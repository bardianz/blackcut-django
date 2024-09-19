# Generated by Django 5.0.4 on 2024-09-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_appointment_is_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('active', 'فعال'), ('done', 'انجام شده'), ('canceled', 'لغو شده'), ('expired', 'منقضی')], default='active', max_length=25),
        ),
    ]
