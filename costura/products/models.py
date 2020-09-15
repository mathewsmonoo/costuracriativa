from django.conf import settings
from django.db import models
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name    = models.CharField("Nome da Categoria", max_length=255, unique=True)
    slug    = AutoSlugField("Category Address", unique=True, populate_from="name")
    image   = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:categories',kwargs={'slug':self.slug})


class Product(TimeStampedModel):
    name        = models.CharField      ("Nome do Produto", max_length=255)
    slug        = AutoSlugField         ("Endereço digital", unique=True, populate_from="name")
    price       = models.DecimalField   ("Preço(R$)",max_digits=8, decimal_places=2,null=True, blank=True) #accepts anything up to R$999,999.99
    sale_price  = models.DecimalField   ("Preço Promocional(R$)",max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField      ("Descrição", default="", blank=True)
    weight      = models.DecimalField   ("Peso(kg)", max_digits=5, decimal_places=2, default=0.1,null=True, blank=True)
    in_stock    = models.BooleanField   ("Disponível?", default=False)
    stock       = models.IntegerField   ("Quantia em estoque", null=True, blank=True, default=0)

    # Relations:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    creator  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    # TODO:
    # Add Discount;
    # Add final price (price - discount);

    def get_price(self):
        if self.sale_price is None:
            return self.price
        else:
            return self.sale_price

    def get_discount(self):
        percentage = ((self.price - self.sale_price)/ self.price) * 100
        holder = str(round(percentage, 2))
        holder = holder.replace(',','.')
        return holder

    class Meta:
        verbose_name="Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail',kwargs={'slug':self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='productimages', on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name="Imagem do Produto"
        verbose_name_plural = "Imagens do Produto"