# Generated by Django 3.0.4 on 2020-06-19 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200521_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variationimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
        migrations.DeleteModel(
            name='VariationImage',
        ),
    ]