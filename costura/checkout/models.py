from django.db import models
#from costura.products.models import Product
from django.conf import settings
from model_utils.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


class Order(TimeStampedModel):
    STATUS_CHOICES = (
        (0, "Aguardando Pagamento"),
        (1, "Compra Concluída"),
        (2, "Compra CANCELADA"),
    )
    slug    = AutoSlugField("Registro digital", unique=True, populate_from="pk")
    user    = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="Usuário", on_delete=models.CASCADE)
    status  = models.IntegerField("Situação", choices=STATUS_CHOICES,default=0, blank=True)
    items   = models.CharField(max_length=1000)
    payment_option   = models.CharField(max_length=1000, default='Deposito')
    address = models.CharField(max_length=1000)
    total   = models.CharField(max_length=200) 
    obs     = models.CharField(max_length=200, default='')
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido # {self.pk}"
    
    def get_absolute_url(self):
        return reverse('checkout:complete',kwargs={'slug':self.slug})
