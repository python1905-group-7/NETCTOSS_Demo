# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-20 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('base_duration', models.CharField(max_length=32, null=True)),
                ('base_cost', models.IntegerField(null=True)),
                ('unit_cost', models.FloatField(null=True)),
                ('status', models.NullBooleanField(default=False)),
                ('descr', models.CharField(max_length=256)),
                ('creatime', models.DateTimeField(auto_now_add=True)),
                ('startime', models.DateTimeField(auto_now=True, null=True)),
                ('cost_type', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'COST',
            },
        ),
    ]
