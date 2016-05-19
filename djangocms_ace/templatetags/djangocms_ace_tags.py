# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import json

from django import template
from django.template.base import Node, token_kwargs
from django.template.loader import render_to_string
from django.templatetags.static import static

from ..models import config_defaults

register = template.Library()


class AceDefaultConfig(object):
   
    def __init__(self):
        self.__dict__.update(**config_defaults)
   
    def __repr__(self):
        return repr(self.__dict__)


class AceEditorNode(Node):
    def __init__(self, nodelist, opts=None):
        self.nodelist = nodelist
        self.opts = opts

    def render(self, context):
        values = {}
        
        config = self.opts['config'].resolve(context) if ('config' in self.opts) else AceDefaultConfig()
        instance = self.opts['instance'].resolve(context) if ('instance' in self.opts) else config

        for opt in config_defaults.keys():
            v = self.opts[opt].resolve(context) if (opt in self.opts) else getattr(instance, opt, getattr(config, opt, config_defaults[opt]))
            values[opt] = v
        
        if (not values['variable_name']):
            values['variable_name'] = 'uuid_' + uuid.uuid4().hex
        
        opts = json.dumps(values)
        
        values['content'] = self.nodelist.render(context)
        values['opts'] = opts
        
        with context.push(**values):
            return render_to_string("djangocms_ace/editor.html", context=context)


@register.tag('with_ace_editor')
def with_ace_editor(parser, token):
    bits = token.split_contents()
    remaining_bits = bits[1:]
    opts = token_kwargs(remaining_bits, parser, support_legacy=True)
    nodelist = parser.parse(('endwith_ace_editor',))
    parser.delete_first_token()
    return AceEditorNode(nodelist, opts)
