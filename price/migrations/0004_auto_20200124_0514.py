# Generated by Django 3.0.2 on 2020-01-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_price_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
