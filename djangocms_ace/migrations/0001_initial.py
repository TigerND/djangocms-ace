# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='AceEditorConfigModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Config name', max_length=32, verbose_name=b'Name')),
                ('theme', models.CharField(default=b'ace/theme/chrome', help_text='Theme module', max_length=32, verbose_name=b'Theme')),
                ('mode', models.CharField(default=b'ace/mode/javascript', help_text='Mode module', max_length=32, verbose_name=b'Mode')),
            ],
            options={
                'verbose_name': 'ACE Editor config',
                'verbose_name_plural': 'ACE Editor configs',
            },
        ),
        migrations.CreateModel(
            name='AceEditorPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('readonly', models.BooleanField(default=True, help_text='Is readonly', verbose_name=b'Readonly')),
                ('content', models.TextField(default=b'', help_text='Content', verbose_name=b'Content')),
                ('theme', models.CharField(blank=True, help_text='Theme module', max_length=32, null=True, verbose_name=b'Theme')),
                ('mode', models.CharField(blank=True, help_text='Mode module', max_length=32, null=True, verbose_name=b'Mode')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangocms_ace.AceEditorConfigModel', verbose_name='Editor config')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
