# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privat24Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='amount')),
                ('ccy', models.CharField(max_length=32, verbose_name='ccy')),
                ('details', models.CharField(max_length=128, verbose_name='details')),
                ('pay_way', models.CharField(max_length=32, verbose_name='pay way')),
                ('order', models.CharField(max_length=64, unique=True, verbose_name='order')),
                ('merchant', models.CharField(max_length=64, verbose_name='merchant')),
                ('state', models.CharField(max_length=32, verbose_name='state')),
                ('date', models.CharField(max_length=64, verbose_name='date')),
                ('signature', models.TextField(verbose_name='signature')),
                ('ext_details', models.CharField(blank=True, max_length=255, null=True, verbose_name='ext details')),
                ('ref', models.CharField(blank=True, max_length=64, null=True, verbose_name='reference')),
                ('payCountry', models.CharField(blank=True, max_length=32, null=True, verbose_name='payCountry')),
                ('sender_phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='sender phone')),
                ('raw_data', models.TextField(blank=True, null=True, verbose_name='raw data')),
            ],
            options={
                'verbose_name': 'privat24 transaction',
                'verbose_name_plural': 'privat24 transactions',
            },
        ),
    ]
