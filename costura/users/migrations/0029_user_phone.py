# Generated by Django 3.0.4 on 2020-12-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20200916_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=13, null=True, verbose_name='Telefone'),
        ),
    ]