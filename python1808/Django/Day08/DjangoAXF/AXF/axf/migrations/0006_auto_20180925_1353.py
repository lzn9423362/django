# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_auto_20180925_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userRank',
            field=models.IntegerField(default=0),
        ),
    ]
