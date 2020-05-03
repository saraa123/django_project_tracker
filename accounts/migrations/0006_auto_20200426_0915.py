# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-26 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200426_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_games',
            field=models.TextField(default='', max_length=200),
        ),
    ]
