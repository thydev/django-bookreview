# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-19 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
