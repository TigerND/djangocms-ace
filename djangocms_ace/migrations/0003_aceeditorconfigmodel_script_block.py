# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_ace', '0002_aceeditorpluginmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceeditorconfigmodel',
            name='script_block',
            field=models.CharField(default=b'js', help_text='Script block', max_length=32, verbose_name=b'Script block'),
        ),
    ]
