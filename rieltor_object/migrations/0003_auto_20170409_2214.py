# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0002_auto_20170409_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='description',
            field=models.TextField(blank=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='building',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building', to='rieltor_object.District'),
        ),
        migrations.AlterField(
            model_name='building',
            name='geo',
            field=models.TextField(blank=True, verbose_name='\u041d\u0430 \u043a\u0430\u0440\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='building',
            name='panorama',
            field=models.TextField(blank=True, verbose_name='\u041f\u0430\u043d\u043e\u0440\u0430\u043c\u0430'),
        ),
    ]