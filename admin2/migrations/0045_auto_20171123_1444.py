# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-23 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0044_emailsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsettings',
            name='name',
            field=models.CharField(default='notify', max_length=20, verbose_name='\u0418\u043c\u044f'),
        ),
    ]
