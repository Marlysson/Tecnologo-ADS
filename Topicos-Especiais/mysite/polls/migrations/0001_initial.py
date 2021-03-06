# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=50)),
                ('closed', models.BooleanField(default=False)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
