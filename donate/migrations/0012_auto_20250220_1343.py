# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2025-02-20 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0011_auto_20250219_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsubscription',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
