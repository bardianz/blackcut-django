# Generated by Django 5.0.4 on 2024-04-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_timeslot_finish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='finish_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
