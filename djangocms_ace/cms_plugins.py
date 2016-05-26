# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2

from django.conf import settings

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import AceEditorPluginModel
from .forms import AceEditorPluginAdminForm

from django.utils.translation import ugettext_lazy as _


class AceEditorPlugin(CMSPluginBase):
    form = AceEditorPluginAdminForm
    name = _('Editor')
    module = _('ACE')
    model = AceEditorPluginModel
    render_template = "djangocms_ace/plugin.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
        return u'//img.shields.io/badge/%s%%20%s-%s-green.svg' % (
            AceEditorPlugin.module,
            AceEditorPlugin.name,
            urllib2.quote(instance.ident),
        )

    def icon_alt(self, instance):
        return u'AceEditor: %s' % instance


plugin_pool.register_plugin(AceEditorPlugin)
