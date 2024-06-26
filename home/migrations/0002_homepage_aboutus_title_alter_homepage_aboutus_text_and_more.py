# Generated by Django 5.0.4 on 2024-05-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='aboutus_title',
            field=models.CharField(default='پیش فرض', max_length=25, verbose_name='عنوان درباره ما'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='aboutus_text',
            field=models.TextField(default='پیش فرض', verbose_name='متن درباره ما'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='address_section',
            field=models.TextField(default='پیش فرض', verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content_1',
            field=models.TextField(default='پیش فرض', verbose_name='محتوا 1'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content_2',
            field=models.TextField(default='پیش فرض', verbose_name='محتوا 2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content_3',
            field=models.TextField(default='پیش فرض', verbose_name='محتوا 3'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='phone_section',
            field=models.TextField(default='پیش فرض', verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='time_section',
            field=models.TextField(default='پیش فرض', verbose_name='تایم کاری'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_1',
            field=models.CharField(default='پیش فرض', max_length=25, verbose_name='عنوان 1'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_2',
            field=models.CharField(default='پیش فرض', max_length=25, verbose_name='عنوان 2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_3',
            field=models.CharField(default='پیش فرض', max_length=25, verbose_name='عنوان 3'),
        ),
    ]
