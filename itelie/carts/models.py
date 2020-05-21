from django.db import models

from itelie.products.models import Variation
# Create your models here.


""" class CartItem(models.Model):
    cart    = models.ForeignKey("Cart", on_delete=models.CASCADE)
    #item    = models.ForeignKey(Variation)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.item.title
    
    def remove(self):
        return self.item.remove_from_cart()
    
 """