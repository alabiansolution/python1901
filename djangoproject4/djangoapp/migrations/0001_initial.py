# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-22 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.Department')),
            ],
        ),
    ]
