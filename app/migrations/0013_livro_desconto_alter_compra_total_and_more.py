# Generated by Django 4.2.4 on 2023-08-25 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='compralivro',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]