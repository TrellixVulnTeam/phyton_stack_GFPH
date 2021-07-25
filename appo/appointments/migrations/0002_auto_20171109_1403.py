# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Missed', 'Missed'), ('Done', 'Done')], max_length=255),
        ),
    ]
