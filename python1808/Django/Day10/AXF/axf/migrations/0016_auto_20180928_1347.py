# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0015_order_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Order'),
        ),
    ]
