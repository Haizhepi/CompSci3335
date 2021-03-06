# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-12-09 04:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181208_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='grad_year',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='middle',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='suffix',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
