# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_smsuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='smsuser',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
