# Generated by Django 2.0.7 on 2019-04-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelcalc', '0002_auto_20190406_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=40)),
                ('car_model', models.CharField(max_length=40)),
                ('car_consumption', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Calculator',
        ),
    ]