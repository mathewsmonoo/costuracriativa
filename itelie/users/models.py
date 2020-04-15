from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from itelie.addresses.models import Address, AddressInfo


class User(AbstractUser):
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    dob     = models.DateField(_("Birthday"), null=True, blank=True)
    cpf     = models.CharField(_("CPF"),max_length=11, default="")   
    rg      = models.CharField(_("RG"),max_length=9, default="")
    phone   = models.CharField(_("Phone Number"), max_length=20, blank=True)
    prefix  = models.CharField(_("Prefix"), max_length=8, blank=True)

    addresses = models.ManyToManyField(Address, through=AddressInfo, through_fields=('user','address'), related_name="user_adresses")

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )

    #  TODO:
    #  ADD RESTRICTIONS
    #  CPF AND RG VALIDATION ; BOTH AS UNIQUE FIELDS
    #  ADD EMPLOYEE MODEL
   
    def __str__(self):
        return self.username
