# Generated by Django 3.0.4 on 2020-04-29 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '0003_auto_20200416_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='owned_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('EE', 'Endereço de Entrega'), ('ES', 'Endereço Secundário')], default='EE', max_length=2, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='extra_data',
            field=models.CharField(blank=True, help_text='Complemento. Exemplo: Ao lado do mercado', max_length=255, null=True, verbose_name='Obs.'),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='address',
            name='nickname',
            field=models.CharField(blank=True, help_text='Identificador. Exemplo: Casa da Praia', max_length=255, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=10, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(help_text='8 Dígitos. Exemplo: 12345-678', max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='address',
            name='receiver_name',
            field=models.CharField(blank=True, help_text='Nome do destinatário', max_length=255, null=True, verbose_name='Destinatário'),
        ),
        migrations.AlterField(
            model_name='address',
            name='receiver_phone',
            field=models.CharField(blank=True, help_text='DDD + n.º. Exemplo: (11) 96123-4567', max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='AC', max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=255, verbose_name='Rua'),
        ),
    ]
