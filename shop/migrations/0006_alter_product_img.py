# Generated by Django 5.0.4 on 2024-04-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='D:\\w\\blackcut-django\\static\\shop\\no-picture.png', upload_to='shop/product/images/', verbose_name='تصویر محصول'),
        ),
    ]
