# Generated by Django 3.2.6 on 2021-12-03 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_alter_sale_book_store_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_book',
            name='store_post_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 3, 17, 57, 54, 459233)),
        ),
    ]
