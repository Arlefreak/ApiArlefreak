# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20160121_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkcategory',
            name='slug',
            field=models.SlugField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectcategory',
            name='slug',
            field=models.SlugField(default=0, editable=False),
            preserve_default=False,
        ),
    ]