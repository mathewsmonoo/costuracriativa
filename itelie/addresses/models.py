from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


ADDRESS_TYPES = (
    ('EE', "Endereço de Entrega"),
    ('ES', "Endereço Secundário"),
)
BRAZILIAN_STATES =(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins')
)

class Address(TimeStampedModel):
    receiver_name   = models.CharField(max_length=255, null=True, blank=True, help_text='Nome do destinatário')
    receiver_phone  = models.CharField(max_length=20,  null=True, blank=True, help_text='DDD + n.º. Exemplo: (11) 96123-4567')
    nickname        = models.CharField(max_length=255, null=False, blank=True, help_text='Identificador. Exemplo: Casa da Praia')
    address_type    = models.CharField(max_length=2, choices=ADDRESS_TYPES, default='EE')
    postal_code     = models.CharField(max_length=8, help_text='8 Dígitos. Exemplo: 12345-678')
    state           = models.CharField(max_length=2, choices=BRAZILIAN_STATES, default='AC')
    city            = models.CharField(max_length=255)
    neighborhood    = models.CharField(max_length=255)
    street          = models.CharField(max_length=255)
    number          = models.CharField(max_length=10)
    extra_data      = models.CharField(max_length=255, null=True, blank=True,help_text='Complemento. Exemplo: Ao lado do mercado')

    def __str__(self):
            return f'{self.nickname}'
    
    def get_absolute_url(self):
        return reverse('addresses:detail', kwargs={"pk": self.pk})

    def get_address(self):
        return f'{self.nickname}\n{self.receiver_name}({self.receiver_phone})\n{self.address_type}\n{self.postal_code} - {self.state},{self.city}\n{self.neighborhood}, {self.street}, {self.number}.\n{self.extra}'


class AddressInfo(models.Model):
    address = models.ForeignKey(Address, on_delete = models.SET_NULL, null=True)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null=True)