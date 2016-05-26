# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.models import ModelForm

from .models import AceEditorPluginModel

from django.utils.translation import ugettext_lazy as _


class AceEditorPluginAdminForm(ModelForm):

    class Meta:
        model = AceEditorPluginModel
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(AceEditorPluginAdminForm, self).__init__(*args, **kwargs)
