from django.db import models
from costura.products.models import Product
from model_utils.models import TimeStampedModel
from django.conf import settings

class CartItemManager(models.Manager):
    # facilita uso do modelo nas views
    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists(): #filtro pelo cart_key e produto
            created     = False
            cart_item   = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created     = True
            cart_item   = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price,sale_price = product.sale_price)
        return cart_item, created

class CartItem(models.Model):
    cart_key    = models.CharField("Chave do Carrinho", max_length=40, db_index=True)
        # ^ associar todos itens de um mesmo carrinho da sessão
    product     = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField("Quantidade", default=1)
    price       = models.DecimalField("Preço(R$)",max_digits=8, decimal_places=2)
    sale_price  = models.DecimalField("Preço Promocional(R$)",max_digits=8, decimal_places=2,blank=True)

    objects = CartItemManager()

    class Meta:
        verbose_name        = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together     = (('cart_key', 'product'),) #indicar que tem o mesmo produto mas com quantia >2 no carrinho

    def __str__(self):
        return f'{self.product},{self.quantity}'

class OrderManager(models.Manager):

    def create_order(self,user,cart_items):
        order = self.create(user=user) #como  cart_items possui default, nao é necessária sua explicitação
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order = order, quantity = cart_item.quantity, product = cart_item.product,price = cart_item.price, sale_price = cart_item.sale_price
            )
        return order

class Order(models.Model):
    STATUS_CHOICES = (
        (0, "Aguardando Pagamento"),
        (1, "Compra Concluída"),
        (2, "Compra CANCELADA"),

    )
    PAYMENT_OPTION_CHOICES=(
        ("deposit",  "Depósito"),
        ("pagseguro","PagSeguro"),
        ("paypal",   "Paypal"),
    )

    user    = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="Usuário", on_delete=models.CASCADE)
    status  = models.IntegerField(
        "Situação", choices=STATUS_CHOICES,default=0, blank=True
    )
    payment_option = models.CharField(
        "Opção de Pagamento", choices=PAYMENT_OPTION_CHOICES, max_length=20, default="deposit" 
    )
     
    created  = models.DateTimeField("Criado em", auto_now_add=True)
    modified = models.DateTimeField("Modificado em", auto_now=True)
    objects  = OrderManager()

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    def __str__(self):
        return f"Pedido # {self.pk}"

class OrderItem(models.Model):
    order   = models.ForeignKey(Order, verbose_name="Pedido", related_name="items",on_delete=models.CASCADE) 
    """toda vez que uma instancia de pedido for criada, ela terá um atributo chamado items, retornando uma qs filtrada so com items associados."""
    product     = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField("Quantidade", default=1)
    # mantem o preço do momento da compra
    price       = models.DecimalField("Preço(R$)",max_digits=8, decimal_places=2,blank=True)
    sale_price  = models.DecimalField("Preço Promocional(R$)",max_digits=8, decimal_places=2,blank=True)

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens dos pedidos"

    def __str__(self):
        return f"Pedido #{self.order}: Produto {self.product}"

def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)