# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['create'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='post',
            name='moder',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]
