# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0008_remove_travelschedule_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelschedule',
            name='join',
            field=models.ManyToManyField(related_name='joined_user', to='belt_app.User'),
        ),
    ]
