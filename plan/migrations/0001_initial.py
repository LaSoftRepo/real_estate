# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u041f\u043b\u0430\u043d\u044b', editable=False, max_length=30, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('title', models.TextField(blank=True, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('SEOTitle', models.TextField(blank=True, null=True, verbose_name='SEO Title')),
                ('SEOKeywords', models.TextField(blank=True, null=True, verbose_name='SEO Keywords')),
                ('SEODescription', models.TextField(blank=True, null=True, verbose_name='SEO Description')),
                ('image', models.ImageField(blank=True, upload_to='background/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('video', models.TextField(blank=True, verbose_name='\u041a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('point1', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0443\u043d\u043a\u0442 1')),
                ('point2', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0443\u043d\u043a\u0442 2')),
                ('point3', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0443\u043d\u043a\u0442 3')),
                ('point4', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0443\u043d\u043a\u0442 4')),
                ('point5', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0443\u043d\u043a\u0442 5')),
            ],
            options={
                'verbose_name': '\u041f\u043b\u0430\u043d\u044b',
            },
        ),
    ]