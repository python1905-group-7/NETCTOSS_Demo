# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-19 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('base_duration', models.IntegerField()),
                ('base_cost', models.FloatField()),
                ('unit_cost', models.FloatField()),
                ('status', models.NullBooleanField()),
                ('descr', models.CharField(max_length=256)),
                ('creatime', models.DateTimeField(auto_now=True)),
                ('startime', models.DateTimeField(null=True)),
                ('cost_type', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'cost',
            },
        ),
    ]