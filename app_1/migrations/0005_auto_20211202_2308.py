# Generated by Django 3.2.9 on 2021-12-02 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_auto_20211202_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_book',
            name='Books_category',
            field=models.CharField(choices=[('Arts & Music', 'Arts & Music'), ('Biographies', 'Biographies'), ('Business', 'Business'), ('Comics', 'Comics'), ('Computers & Tech', 'Computers & Tech'), ('Cooking', 'Cooking'), ('Edu & Reference', 'Edu & Reference'), ('Entertainment', 'Entertainment'), ('Special Editions', 'Special Editions'), ('Health & Fitness', 'Health & Fitness'), ('History', 'History'), ('Horror', 'Horror'), ('Medical', 'Medical'), ('Religion', 'Religion'), ('Romance', 'Romance'), ('Other', 'Other')], default='All', max_length=90),
        ),
        migrations.AlterField(
            model_name='sale_book',
            name='store_post_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 23, 8, 35, 398806)),
        ),
    ]
