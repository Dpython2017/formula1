# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicRaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastest_laps',
            name='time_taken',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
