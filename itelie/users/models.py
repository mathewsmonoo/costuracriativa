from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
#from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
#import datetime

class User(AbstractUser):
    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )

    dob = models.DateTimeField(_("Birthday"), auto_now=False, blank=True, null=True)
    
   
    cpf = models.CharField(_("CPF"),max_length=11, default="")   
    rg = models.CharField(_("RG"),max_length=9, default="")
    
    phone = models.CharField(_("Phone Number"), max_length=20, blank=True)

    prefix = models.CharField(_("Prefix"), max_length=8, blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
    #  TODO:
    #  ADD RESTRICTIONS
    #  CPF AND RG VALIDATION AND AS UNIQUE FIELDS
    #  ADD EMPLOYEE MODEL

""" class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = )
 """