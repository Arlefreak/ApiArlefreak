# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0013_podcast_feedburner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='audio_size',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
