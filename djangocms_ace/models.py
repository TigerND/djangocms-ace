# -*- coding: utf-8 -*-

import json

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.utils.compat.dj import python_2_unicode_compatible


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
        default=getattr(settings, 'ACE_EDITOR_DEFAULT_THEME', 'ace/theme/chrome'),
        help_text=_(u'Theme module'),
        max_length=32,
    )

    mode = models.CharField('Mode',
        null=False,
        blank=False,
        default=getattr(settings, 'ACE_EDITOR_DEFAULT_MODE', 'ace/mode/javascript'),
        help_text=_(u'Mode module'),
        max_length=32,
    )

    script_block = models.CharField('Script block',
        null=False,
        blank=False,
        default='js',
        help_text=_(u'Script block'),
        max_length=32,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('ACE Editor config')
        verbose_name_plural = _('ACE Editor configs')


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

    def ident(self):
        return self.name if self.name else str(self.id)

    readonly = models.BooleanField('Readonly',
        null=False,
        blank=False,
        default=True,
        help_text=_(u'Is readonly'),
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

    def editor_theme(self):
        return self.theme if self.theme else self.config.theme

    mode = models.CharField('Mode',
        null=True,
        blank=True,
        help_text=_(u'Mode module'),
        max_length=32,
    )

    def editor_mode(self):
        return self.mode if self.mode else self.config.mode

    def variable_name(self):
        return 'djangocms_ace_editor_' + self.ident()

    def script_block(self):
        return self.config.script_block
        
    def opts(self):
        result = {
            'ident': self.ident(),
            'variable_name': self.variable_name(),
            'theme': self.editor_theme(),
            'mode': self.editor_mode(),
            'readonly': self.readonly,
        }
        return json.dumps(result)

    def __str__(self):
        return _(u'AceEditor %(ident)s') % {'ident': self.ident()}
