# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-16 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='tel_user_phone',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
