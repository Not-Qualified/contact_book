# Generated by Django 3.0.2 on 2020-01-24 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_auto_20200124_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]