# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0008_auto_20170514_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earth',
            name='contact_name',
        ),
    ]
