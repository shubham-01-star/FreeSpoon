# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0029_auto_20160620_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bulk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Bulk'),
        ),
    ]