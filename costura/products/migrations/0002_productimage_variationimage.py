# Generated by Django 3.0.4 on 2020-05-21 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='variations/%Y/%m/%d')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='variationimages', to='products.Variation')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='productimages', to='products.Product')),
            ],
        ),
    ]