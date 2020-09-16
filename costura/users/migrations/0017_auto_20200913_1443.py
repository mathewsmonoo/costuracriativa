# Generated by Django 3.0.4 on 2020-09-13 17:43

import costura.users.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cpf',
            field=models.CharField(default='', max_length=14, unique=True, validators=[costura.users.validators.validate_cpf], verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default='2020-01-01', verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='join_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lname',
            field=models.CharField(blank=True, max_length=255, verbose_name='User Last Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]