from django.db import models
from costura.products.models import Product
from model_utils.models import TimeStampedModel


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

def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)