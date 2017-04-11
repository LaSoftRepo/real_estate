# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('price', models.IntegerField(blank=True, verbose_name='\u0426\u0435\u043d\u0430')),
                ('type_deal', models.IntegerField(blank=True, choices=[(1, '\u0410\u0440\u0435\u043d\u0434\u0430'), (2, '\u041f\u0440\u043e\u0434\u0430\u0436\u0430')], verbose_name='\u0422\u0438\u043f')),
                ('appointment', models.IntegerField(blank=True, choices=[(1, '\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'), (2, '\u0414\u043e\u043c')], verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('footage', models.IntegerField(blank=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('rooms', models.IntegerField(blank=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442')),
                ('point', models.IntegerField(verbose_name='\u0411\u0430\u043b\u044b')),
                ('when_create', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('location', models.IntegerField(blank=True, choices=[(1, '\u0424\u0430\u0441\u0430\u0434'), (2, '\u0414\u0432\u043e\u0440\u043e\u0432\u043e\u0439'), (3, '\u0411\u0438\u0437\u043d\u0435\u0441-\u0446\u0435\u043d\u0442\u0440')], verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435')),
                ('floor', models.IntegerField(blank=True, choices=[(1, '1-\u0439'), (2, '\u0426\u043e\u043a\u043e\u043b\u044c'), (3, '\u0411\u0435\u043b\u044c\u044d\u0442\u0430\u0436')], verbose_name='\u042d\u0442\u0430\u0436')),
                ('entrance', models.IntegerField(blank=True, choices=[(1, '1-\u0439'), (2, '\u0426\u043e\u043a\u043e\u043b\u044c'), (3, '\u0411\u0435\u043b\u044c\u044d\u0442\u0430\u0436')], verbose_name='\u0412\u0445\u043e\u0434')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('panorama', models.TextField(verbose_name='\u041f\u0430\u043d\u043e\u0440\u0430\u043c\u0430')),
                ('geo', models.TextField(verbose_name='\u041d\u0430 \u043a\u0430\u0440\u0442\u0435')),
                ('views', models.IntegerField(default=0, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u044b')),
            ],
            options={
                'verbose_name': '\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u044b \u0438 \u0414\u043e\u043c\u0430',
                'verbose_name_plural': '\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u044b \u0438 \u0414\u043e\u043c\u0430',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0439\u043e\u043d',
                'verbose_name_plural': '\u0420\u0430\u0439\u043e\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building', to='rieltor_object.District'),
        ),
    ]