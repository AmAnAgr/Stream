# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]