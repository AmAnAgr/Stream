# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20170330_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]