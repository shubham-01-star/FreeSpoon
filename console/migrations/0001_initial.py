# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField()),
                ('status', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('spec', models.CharField(max_length=200)),
                ('stock', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/commodity/%Y/%m/%d')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='CommodityInBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quota', models.IntegerField(max_length=10)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Batch')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='CommodityInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=200)),
                ('id_wechat', models.CharField(max_length=200, unique=True)),
                ('tel', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distributer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=13, unique=True)),
                ('tel', models.CharField(max_length=20, unique=True)),
                ('id_wechat', models.CharField(max_length=200, unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
                ('tail', models.CharField(blank=True, max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=13, unique=True)),
                ('tel', models.CharField(max_length=20, unique=True)),
                ('id_wechat', models.CharField(max_length=200, unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
                ('tail', models.CharField(blank=True, max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('successful_times', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(max_length=10)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Batch')),
                ('commodities', models.ManyToManyField(through='console.CommodityInOrder', to='console.Commodity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='commodityinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Order'),
        ),
        migrations.AddField(
            model_name='batch',
            name='commodities',
            field=models.ManyToManyField(through='console.CommodityInBatch', to='console.Commodity'),
        ),
        migrations.AddField(
            model_name='batch',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Leader'),
        ),
    ]