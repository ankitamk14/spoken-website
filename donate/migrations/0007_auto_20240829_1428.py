# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-08-29 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_testattendance_mdlgrade'),
        ('donate', '0006_payee_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationpayee',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donationpayee',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodies',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodies',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donationpayee',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goodies',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
