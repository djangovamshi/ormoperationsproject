# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-10-08 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
