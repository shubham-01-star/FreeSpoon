# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0058_remove_bulk_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulk',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
            preserve_default=False,
        ),
    ]
