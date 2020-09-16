# Generated by Django 3.0.4 on 2020-09-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20200916_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
