# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-12 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo', '0009_remove_deal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
