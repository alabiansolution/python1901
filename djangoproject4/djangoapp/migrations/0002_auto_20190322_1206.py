# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-22 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Topic',
        ),
    ]