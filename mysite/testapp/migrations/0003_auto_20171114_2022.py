# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-14 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20171114_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitemnormal2',
            name='text',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='shoppingitemnormal2',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]