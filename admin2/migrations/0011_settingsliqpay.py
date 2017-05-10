# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0010_auto_20170510_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsLiqpay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant', models.IntegerField(blank=True, null=True, verbose_name='Liqpay merchant ID')),
                ('signature', models.CharField(blank=True, max_length=250, null=True, verbose_name='Liqpay signature')),
                ('currency', models.CharField(blank=True, choices=[('UAH', 'UAH'), ('RUB', 'RUB'), ('USD', 'USD')], max_length=3, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
