# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-04 20:15
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tattoo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TattooImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.ImageField(default='/home/jops/university/refactoring/vtattoo/media/tattooimg/cup.jpg', storage=django.core.files.storage.FileSystemStorage('/home/jops/university/refactoring/vtattoo/media/tattooimg'), upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tattoo',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='tattoo',
            name='image_file',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tattoo.TattooImageUpload'),
        ),
    ]
