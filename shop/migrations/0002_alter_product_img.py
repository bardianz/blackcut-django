# Generated by Django 5.0.4 on 2024-04-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='shop/product/images/'),
        ),
    ]
