# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-27 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0008_auto_20190927_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name=models.BooleanField(default=False)),
        ),
    ]
