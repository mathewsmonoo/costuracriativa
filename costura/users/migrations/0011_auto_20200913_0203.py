# Generated by Django 3.0.4 on 2020-09-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200913_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_number',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ID do Colaborador'),
        ),
    ]
