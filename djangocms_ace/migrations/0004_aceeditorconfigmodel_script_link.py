# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_ace', '0003_aceeditorconfigmodel_script_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceeditorconfigmodel',
            name='script_link',
            field=models.CharField(default=b'/static/djangocms_ace/ace/ace.js', help_text='Script link', max_length=256, verbose_name=b'Script link'),
        ),
    ]
