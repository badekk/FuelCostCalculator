# Generated by Django 2.0.7 on 2019-04-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuelcalc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculator',
            old_name='city_a',
            new_name='destination_city',
        ),
        migrations.RenameField(
            model_name='calculator',
            old_name='city_b',
            new_name='start_city',
        ),
    ]
