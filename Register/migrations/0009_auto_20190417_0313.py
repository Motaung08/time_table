# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-17 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0008_auto_20190408_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='CellPhone_No',
        ),
        migrations.RemoveField(
            model_name='studentsregister',
            name='CellPhone_No',
        ),
    ]
