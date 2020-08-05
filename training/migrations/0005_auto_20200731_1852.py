# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-31 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_merge_20200729_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='trainingevents',
            name='event_type',
            field=models.CharField(choices=[('', '-----'), ('FDP', 'Paid FDP'), ('Workshop', 'Blended Mode Workshop'), ('sdp', 'Student Training Programme')], max_length=50),
        ),
        migrations.AddField(
            model_name='eventattendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.TrainingEvents'),
        ),
        migrations.AddField(
            model_name='eventattendance',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.Participant'),
        ),
    ]