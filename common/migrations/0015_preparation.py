# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_whatyouknown'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]