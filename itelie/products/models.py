from django.conf import settings
from django.db import models
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from model_utils.models import TimeStampedModel


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
    color       = models.CharField("Color", max_length=255)
    cost        = models.DecimalField("Cost(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    price       = models.DecimalField("Price(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    promo_price = models.DecimalField("Promotional Price(R$)",max_digits=8, decimal_places=2, null=True, blank=True) #accepts anything up to R$999,999.99
    description = models.TextField("Product Description", default="", blank=True)
    weight      = models.DecimalField("Weight of Product (kg)", max_digits=5, decimal_places=2, default=0.1)
    status      = models.BooleanField("Product Available?", default=True)
    slug        = AutoSlugField("Product Address", unique=True, populate_from="name")
    #image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)

    # Relations:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    
    # TODO: 
    # Transform COLOR field into list ;
    # OK - Add Category relationship;
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail',kwargs={'slug':self.slug})

    def get_profit(self):
        profit = self.price - self.cost
        return profit

class Variation(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    name        = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active      = models.BooleanField(default=True)
    inventory   = models.PositiveIntegerField("Quantity in Stock", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.prince

""" def add_to_cart(self):
		return "%s?item=%s&qty=1" %(reverse("cart"), self.id) #here cart is url name

	def remove_from_cart(self):
		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

	def get_title(self):
		return "%s - %s" %(self.product.title, self.title)
 """