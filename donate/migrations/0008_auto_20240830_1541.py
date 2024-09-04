# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-08-30 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_testattendance_mdlgrade'),
        ('donate', '0007_auto_20240829_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('gender', models.CharField(choices=[('', '--- Gender ---'), ('M', 'Male'), ('F', 'Female'), ('O', "Don't wish to disclose")], max_length=6)),
                ('contact', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'USA')], default='India', max_length=6)),
                ('reqId', models.CharField(default='', max_length=100)),
                ('note', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.State')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='donationpayee',
            name='city',
        ),
        migrations.RemoveField(
            model_name='donationpayee',
            name='state',
        ),
        migrations.RemoveField(
            model_name='goodies',
            name='city',
        ),
        migrations.RemoveField(
            model_name='goodies',
            name='state',
        ),
        migrations.AlterField(
            model_name='donationpayee',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='goodies',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
