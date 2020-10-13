import re

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .validators import username_validator, validate_cpf

class User(AbstractUser,PermissionsMixin): #This is the "Customer" user; 
    is_superuser = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_customer  = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    join_date    = models.DateField(auto_now_add=True)
    prefix       = models.CharField(_("Prefixo / Apelido"), max_length=8, blank=True)
    cpf          = models.CharField(_("CPF"), max_length=14, validators=[validate_cpf])#,unique=True)
    dob          = models.DateField("Data de Nascimento", null=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.first_name}
        )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.first_name 

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','cpf','dob',]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        return self.user.username

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