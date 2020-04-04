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

    surname = models.CharField(blank=True, max_length=255)
    bio = models.TextField(default="")
    
    cpf = models.CharField(max_length=11)   
        # FIX - ADD UNIQUE FIELD AND CPF VALIDATION
    rg = models.CharField(max_length=9)     
        # FIX - ADD UNIQUE FIELD

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
