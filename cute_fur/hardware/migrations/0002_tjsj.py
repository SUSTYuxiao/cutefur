# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tjsj',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('data', models.IntegerField(default=0)),
            ],
        ),
    ]
