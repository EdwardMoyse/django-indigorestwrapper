# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device1History',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(blank=True, null=True)),
                ('sensitivity', models.IntegerField(blank=True, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('state_active', models.NullBooleanField()),
                ('state_disconnected', models.NullBooleanField()),
                ('state_passive', models.NullBooleanField()),
                ('state_preparing', models.NullBooleanField()),
                ('state_unavailable', models.NullBooleanField()),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': '',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device2History',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(blank=True, null=True)),
                ('onoffstate', models.NullBooleanField()),
            ],
            options={
                'db_table': '',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device3History',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(blank=True, null=True)),
                ('onoffstate', models.NullBooleanField()),
                ('sensorvalue', models.IntegerField(blank=True, null=True)),
                ('sensorvalue_ui', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': '',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device4History',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(blank=True, null=True)),
                ('onoffstate', models.NullBooleanField()),
                ('batterylevel', models.IntegerField(blank=True, null=True)),
                ('batterylevel_ui', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': '',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('modelpk', models.AutoField(primary_key=True, serialize=False)),
                ('lastChangedTimeStr', models.CharField(max_length=32)),
                ('typeSupportsHVAC', models.BooleanField()),
                ('hasStateToDisplay', models.BooleanField()),
                ('typeSupportsEnergyMeter', models.BooleanField()),
                ('typeSupportsIO', models.BooleanField()),
                ('id', models.IntegerField()),
                ('typeFlags', models.IntegerField()),
                ('typeSupportsOnOff', models.BooleanField()),
                ('addressStr', models.CharField(max_length=32)),
                ('typeSupportsSensorValue', models.BooleanField()),
                ('type', models.CharField(max_length=128)),
                ('classID', models.IntegerField()),
                ('displayRawState', models.CharField(max_length=32)),
                ('typeSupportsSpeedControl', models.BooleanField()),
                ('displayInUI', models.BooleanField()),
                ('displayLongState', models.CharField(max_length=32)),
                ('restParent', models.CharField(max_length=32)),
                ('address', models.IntegerField()),
                ('versByte', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('lastChanged', models.IntegerField()),
                ('typeSupportsDim', models.BooleanField()),
                ('lastChangedDateStr', models.DateField()),
                ('lastChangedRFC3339', models.DateTimeField()),
                ('devProtocol', models.IntegerField()),
                ('folderID', models.IntegerField()),
                ('typeSupportsSprinkler', models.BooleanField()),
            ],
        ),
    ]
