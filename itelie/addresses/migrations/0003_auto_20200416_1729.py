# Generated by Django 3.0.4 on 2020-04-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20200415_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('EE', 'Endereço de Entrega'), ('ES', 'Endereço Secundário')], default='EE', max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='extra_data',
            field=models.CharField(blank=True, help_text='Complemento. Exemplo: Ao lado do mercado', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='nickname',
            field=models.CharField(blank=True, help_text='Identificador. Exemplo: Casa da Praia', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(help_text='8 Dígitos. Exemplo: 12345-678', max_length=8),
        ),
        migrations.AlterField(
            model_name='address',
            name='receiver_phone',
            field=models.CharField(blank=True, help_text='DDD + n.º. Exemplo: (11) 96123-4567', max_length=20, null=True),
        ),
    ]
