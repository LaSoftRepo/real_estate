# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesRieltor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('SEOTitle', models.TextField(blank=True, null=True, verbose_name='SEO Title')),
                ('SEOKeywords', models.TextField(blank=True, null=True, verbose_name='SEO Keywords')),
                ('SEODescription', models.TextField(blank=True, null=True, verbose_name='SEO Description')),
                ('image', models.ImageField(blank=True, upload_to='services/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('is_enable', models.BooleanField(default=True, verbose_name='\u0412\u043b\u044e\u0447\u0435\u043d \u043b\u0438?')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0438 \u0440\u0438\u0435\u043b\u0442\u043e\u0440\u0441\u043a\u0438\u0435',
            },
        ),
    ]