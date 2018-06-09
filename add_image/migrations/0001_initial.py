# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('img', models.ImageField(upload_to='images', verbose_name='Картинка')),
            ],
            options={
                'db_table': 'img_add',
                'verbose_name': 'Добавить картинку',
            },
        ),
    ]