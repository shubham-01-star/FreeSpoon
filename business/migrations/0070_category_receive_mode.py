# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0069_auto_20160829_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='receive_mode',
            field=models.IntegerField(default=2, max_length=11),
        ),
    ]
