# Generated by Django 5.1.3 on 2024-11-23 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_description_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='incoming_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 23, 20, 9, 31, 75682)),
        ),
    ]