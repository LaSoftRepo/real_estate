# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0013_auto_20170425_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='trustpagemodel',
            name='faq_enable',
            field=models.BooleanField(default=True, verbose_name='\u0412\u043b\u044e\u0447\u0435\u043d \u043b\u0438 FAQ?'),
        ),
    ]
