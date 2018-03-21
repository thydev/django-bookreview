# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-20 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reivews', to='books.Book'),
        ),
        migrations.AlterField(
            model_name='book_review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='login.User'),
        ),
    ]
