from django.conf import settings
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name    = models.CharField("Name of Category", max_length=255)
    slug    = AutoSlugField("Category Address", unique=True, populate_from="name")

    # TODO:
    # Add Image;

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('shop:product_list_by_category,kwargs={'slug':self.slug})
        #return reverse('products:product_list_by_category,kwargs={'slug':self.slug})
        pass


class Product(TimeStampedModel):
    name    = models.CharField("Name of Product", max_length=255)
    color   = models.CharField("Color", max_length=255)
    cost    = models.DecimalField("Cost(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    price   = models.DecimalField("Price(R$)",max_digits=8, decimal_places=2) #accepts anything up to R$999,999.99
    inventory = models.PositiveIntegerField("Quantity in Stock")
    description = models.TextField("Product Description", default="", blank=True)
    weight  = models.DecimalField("Weight of Product (kg)", max_digits=5, decimal_places=2, default=0.1)
    status  = models.BooleanField("Product Available?", default=True)
    slug    = AutoSlugField("Product Address", unique=True, populate_from="name")

    # Relations:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)

    # TODO: 
    # Transform COLOR field into list ; 
    # Add Category relationship;
    # Add Discount;
    # Add final price (price - discount);
    # Add Images;
    # Add creator field to check which user added product to database
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        #ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail',kwargs={'slug':self.slug})

    def get_profit(self):
        profit = self.price - self.cost
        return profit

    def get_final_price(self):
        pass
