# Generated by Django 3.0.4 on 2020-05-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage_variationimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Imagem do Produto', 'verbose_name_plural': 'Imagens do Produto'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nome da Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.1, max_digits=5, null=True, verbose_name='Peso(kg)'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço Promocional'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='stock',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Quantia em estoque'),
        ),
    ]