# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransferApp', '0002_auto_20170507_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
