# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-16 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20180116_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='hotel',
            field=models.CharField(choices=[('Алмаз-Плюс', 'Алмаз'), ('Алмаз-Плюс', 'Алмаз-Плюс')], max_length=200),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='room_class',
            field=models.CharField(choices=[('Стандарт', 'Стандарт'), ('Напівлюкс', 'Напівлюкс'), ('Люкс', 'Люкс')], max_length=200),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='tel_user_phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
