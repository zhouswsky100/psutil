# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='psutil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('cpuCore', models.CharField(max_length=20)),
                ('cpuLineCity', models.CharField(max_length=20)),
                ('hardDiskSize', models.CharField(max_length=20)),
                ('hardDiskLimit', models.CharField(max_length=20)),
            ],
        ),
    ]
