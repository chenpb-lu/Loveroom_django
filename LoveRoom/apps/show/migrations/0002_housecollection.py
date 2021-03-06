# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-25 16:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_auto_20190815_1033'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='收藏/取消时间')),
                ('status', models.BooleanField(default=True, verbose_name='收藏状态')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_collection_set', to='house.HouseInfo', verbose_name='房源')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_collection_set', to=settings.AUTH_USER_MODEL, verbose_name='收藏者')),
            ],
        ),
    ]
