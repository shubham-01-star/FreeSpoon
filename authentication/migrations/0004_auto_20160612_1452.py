# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20160601_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobuser',
            name='mob',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
