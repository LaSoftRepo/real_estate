# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privat24', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
