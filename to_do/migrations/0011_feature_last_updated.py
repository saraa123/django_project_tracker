# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-25 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0010_auto_20191019_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
