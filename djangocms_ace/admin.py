# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import AceEditorConfigModel


class AceEditorConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(AceEditorConfigModel, AceEditorConfigAdmin)
