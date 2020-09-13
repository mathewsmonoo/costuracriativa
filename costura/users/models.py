import re

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .validators import username_validator, validate_cpf

class User(AbstractUser,PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
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
    

    """ 
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Customer(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
     """
    """
    join_date   = models.DateField(auto_now_add=True)
    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[username_validator], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField(("Nome do Usuário"), blank=True, max_length=255)
    email = models.EmailField("E-mail", unique=True)
    dob = models.DateField(_("Nascimento"), null=True, blank=True)
    cpf = models.CharField(_("CPF"), max_length=14, validators=[validate_cpf], default="")
    rg = models.CharField(_("RG"), max_length=9, default="")
    phone = models.CharField(_("Numero de Telefone"), max_length=20, blank=True)
    prefix = models.CharField(_("Prefixo"), max_length=8, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    """
