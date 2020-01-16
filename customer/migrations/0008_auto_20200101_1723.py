# Generated by Django 3.0.1 on 2020-01-01 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20200101_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Only Alphabets Allowed', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='job',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Only Alphabets Allowed', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Only Alphabets Allowed', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Only Alphabets Allowed', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Enter Valid Six Digit PinCode', regex='^[1-9]\\d{5}$')]),
        ),
    ]