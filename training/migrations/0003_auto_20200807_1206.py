# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-08-07 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0002_auto_20200806_1237'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('event', 'user')]),
        ),
    ]
