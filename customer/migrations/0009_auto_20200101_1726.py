# Generated by Django 3.0.1 on 2020-01-01 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20200101_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator(message='Enter Valid Six Digit PinCode', regex='^[1-9]\\d{5}$')]),
        ),
    ]