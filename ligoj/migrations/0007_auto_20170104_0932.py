# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-04 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligoj', '0006_remove_link_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-date_created']},
        ),
    ]
