from django.conf import settings
from django.db import models
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from model_utils.models import TimeStampedModel
from utils import utils



class Category(TimeStampedModel):
    name    = models.CharField("Name of Category", max_length=255, unique=True)
    slug    = AutoSlugField("Category Address", unique=True, populate_from="name")

    # TODO:
    # Add Image;

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural= 'categories'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:categories',kwargs={'slug':self.slug})


class Product(TimeStampedModel):
    name        = models.CharField("Product name", max_length=255)
    cost        = models.DecimalField("Cost(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    price       = models.DecimalField("Price(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    sale_price  = models.DecimalField("Promotional Price(R$)",max_digits=8, decimal_places=2, null=True, blank=True) #accepts anything up to R$999,999.99
    description = models.TextField("Product Description", default="", blank=True)
    weight      = models.DecimalField("Weight of Product (kg)", max_digits=5, decimal_places=2, default=0.1)
    status      = models.BooleanField("Product Available?", default=True)
    slug        = AutoSlugField("Product Address", unique=True, populate_from="name")
    #image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)

    # Relations:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    
    # TODO: 
    # Transform COLOR field into list ;
    # OK - Add Category relationship ;
    # Add Discount;
    # Add final price (price - discount);
    # Add Images;
    # Add creator field to check which user added product to database;
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def get_formatted_price(self):
        return utils.price_format(self.price)
    get_formatted_price.short_description = 'Price'

    def get_formatted_sale_price(self):
        return utils.price_format(self.sale_price)
    get_formatted_sale_price.short_description = 'Sale Price'

    def get_absolute_url(self):
        return reverse('products:detail',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{self.name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Variation(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    name        = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active      = models.BooleanField(default=True)
    stock       = models.PositiveIntegerField("Quantity in Stock", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'