# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-12-09 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181208_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
