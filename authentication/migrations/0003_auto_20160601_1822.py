# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_mobuser_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobuser',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='mobuser',
            name='name',
        ),
    ]