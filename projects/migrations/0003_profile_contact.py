# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-24 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190524_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(default=0),
        ),
    ]