# Generated by Django 3.2.9 on 2021-12-02 12:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sale_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_post_book_name', models.CharField(max_length=256)),
                ('store_post_book_user_email', models.CharField(max_length=256)),
                ('store_post_book_user_number', models.CharField(max_length=256)),
                ('store_post_book_subject', models.CharField(max_length=256)),
                ('store_post_book_description', models.TextField(max_length=256)),
                ('store_post_time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 18, 52, 34, 657983))),
                ('store_user', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sale Book Information',
            },
        ),
    ]
