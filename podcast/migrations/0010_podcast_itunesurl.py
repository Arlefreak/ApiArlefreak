# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0009_auto_20170526_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='iTunesURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
