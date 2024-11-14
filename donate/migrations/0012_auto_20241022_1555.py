# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-10-22 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donate', '0011_auto_20241016_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='FossSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqId', models.CharField(default='', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('mail_status', models.BooleanField(default=False)),
                ('mail_response', models.CharField(max_length=250)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FossSubscriptionTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestType', models.CharField(max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reqId', models.CharField(max_length=50)),
                ('transId', models.CharField(max_length=100)),
                ('refNo', models.CharField(max_length=50)),
                ('provId', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=2)),
                ('msg', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paymentdetail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='donate.FossSubscription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='usersubscriptiontransactions',
            name='paymentdetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='donate.UserSubscription'),
        ),
    ]
