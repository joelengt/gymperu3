# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0004_auto_20160325_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aerobicos',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='bestcyclng',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='clases',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='deportesdecontacto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='talleres',
            name='imagen',
        ),
    ]
