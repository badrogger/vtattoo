# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo', '0004_auto_20171205_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='tatooStudio',
            new_name='tattoo_studio',
        ),
        migrations.RenameField(
            model_name='tattoo',
            old_name='image_file',
            new_name='image',
        ),
    ]
