# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-02 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kami',
            field=models.TextField(default='www.abc.com'),
        ),
    ]