# -*- coding: utf-8 -*-

import os
import json

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.templatetags.static import static
from cms.utils.compat.dj import python_2_unicode_compatible


config_defaults = {
    'script_block': getattr(settings, 'ACE_EDITOR_SCRIPT_BLOCK', 'js'),
    'script_link': getattr(settings, 'ACE_EDITOR_SCRIPT_LINK', static('djangocms_ace/ace/ace.js')),
    'theme': getattr(settings, 'ACE_EDITOR_DEFAULT_THEME', 'ace/theme/chrome'),
    'mode': getattr(settings, 'ACE_EDITOR_DEFAULT_MODE', 'ace/mode/plain_text'),
    'variable_name': None,
    'readonly': True,
}


@python_2_unicode_compatible
class AceEditorConfigModel(models.Model):
    
    name = models.CharField('Name',
        null=False,
        blank=False,
        help_text=_(u'Config name'),
        max_length=32,
    )

    theme = models.CharField('Theme',
        null=False,
        blank=False,
        default=config_defaults['theme'],
        help_text=_(u'Theme module'),
        max_length=32,
    )

    mode = models.CharField('Mode',
        null=False,
        blank=False,
        default=config_defaults['mode'],
        help_text=_(u'Mode module'),
        max_length=32,
    )

    script_block = models.CharField('Script block',
        null=False,
        blank=False,
        default=config_defaults['script_block'],
        help_text=_(u'Script block'),
        max_length=32,
    )

    script_link = models.CharField('Script link',
        null=False,
        blank=False,
        default=config_defaults['script_link'],
        help_text=_(u'Script link'),
        max_length=256,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ace Editor config')
        verbose_name_plural = _('Ace Editor configs')


@python_2_unicode_compatible
class AceEditorPluginModel(CMSPlugin):

    config = models.ForeignKey(AceEditorConfigModel,
        null=False,
        blank=False,
        verbose_name=_('Editor config')
    )

    name = models.CharField('Name',
        null=True,
        blank=True,
        help_text=_(u'Name'),
        max_length=32,
    )

    @property
    def ident(self):
        return self.name if self.name else str(self.id)

    readonly = models.BooleanField('Readonly',
        null=False,
        blank=False,
        default=True,
        help_text=_(u'Readonly'),
    )

    content = models.TextField('Content',
        null=False,
        blank=False,
        default='',
        help_text=_(u'Content'),
    )

    theme = models.CharField('Theme',
        null=True,
        blank=True,
        help_text=_(u'Theme module'),
        max_length=32,
    )

    @property
    def editor_theme(self):
        return self.theme if self.theme else self.config.theme

    mode = models.CharField('Mode',
        null=True,
        blank=True,
        help_text=_(u'Mode module'),
        max_length=32,
    )

    @property
    def editor_mode(self):
        return self.mode if self.mode else self.config.mode

    @property
    def variable_name(self):
        return 'djangocms_ace_editor_' + self.ident

    @property
    def script_block(self):
        return self.config.script_block
        
    @property
    def script_link(self):
        return self.config.script_link

    @property
    def opts(self):
        result = {
            'ident': self.ident,
            'variable_name': self.variable_name,
            'theme': self.editor_theme,
            'mode': self.editor_mode,
            'readonly': self.readonly,
        }
        return json.dumps(result)

    def __str__(self):
        return _(u'AceEditor %(ident)s') % {'ident': self.ident}
