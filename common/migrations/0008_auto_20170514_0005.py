# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20170513_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='source',
            field=models.TextField(max_length=150, verbose_name='\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a'),
        ),
    ]