# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('girl_num', models.PositiveIntegerField()),
                ('boy_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
