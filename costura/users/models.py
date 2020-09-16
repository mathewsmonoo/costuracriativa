import re

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .validators import username_validator, validate_cpf

class User(AbstractUser,PermissionsMixin): #This is the "Customer" user; 
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True) # Default set as 1 and will change whanever a custom user ("subclassed") is created.
    is_active = models.BooleanField(default=True)
    join_date = models.DateField(auto_now_add=True)
    email = models.EmailField("E-mail", unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    lname = models.CharField(_("User Last Name"), blank=True, max_length=255)
    cpf = models.CharField(_("CPF"), max_length=14, validators=[validate_cpf])#,unique=True)
    dob = models.DateField("Data de Nascimento", null=True , blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.name}
        )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','lname','cpf','dob']

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"
        
    def __str__(self):
        return self.user.username
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        
    def __str__(self):
        return self.user.username