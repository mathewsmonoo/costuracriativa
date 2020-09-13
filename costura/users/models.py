import re

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .validators import username_validator, validate_cpf


class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField("Equipe", default=False, blank=True, null=True)
    is_active = models.BooleanField("Ativo",  default=True)

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

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

# class Staff(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     staff_number = models.PositiveIntegerField(blank=True,n)

# class Costumer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     user_nickname = models.CharField("Nick", max_length=25, default="", blank=True)
