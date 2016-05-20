# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import json

from django import template
from django.template.base import FilterExpression, Node, token_kwargs
from django.template.loader import render_to_string
from django.templatetags.static import static
from ..models import config_defaults

register = template.Library()


def render_ace_editor(context, extra_context=None, **kwargs):
    
    def _resolve(v):
        return v.resolve(context) if isinstance(v, (FilterExpression,)) else v
    
    config = kwargs['config'] if ('config' in kwargs) else AceDefaultConfig()
    instance = kwargs['instance'] if ('instance' in kwargs) else config

    values = {}
    for opt in config_defaults.keys():
        v = _resolve(kwargs[opt] if (opt in kwargs) else getattr(instance, opt, getattr(config, opt, config_defaults[opt])))
        values[opt] = v
    
    if (not values['variable_name']):
        values['variable_name'] = 'uuid_' + uuid.uuid4().hex
    
    opts = json.dumps(values)
    
    values['opts'] = opts
    
    with context.push(**values):
        with context.push(**extra_context):
            return render_to_string("djangocms_ace/editor.html", context=context)


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
        extra_context = {
            'content': self.nodelist.render(context)
        }

        return render_ace_editor(context, extra_context=extra_context, **self.opts)
        

@register.simple_tag(takes_context=True)
def ace_editor(context, content=None, **kwargs):
    """
    Examples:

        {% load djangocms_ace_tags %}

        {% ace_editor content='console.log("Hello World");' %}
        
        {% ace_editor config=config.ace_config content='console.log("Hello World");' %}
        
        {% ace_editor config=config.ace_config theme="ace/theme/solarized_light" content='console.log("Hello World");' %}
    """

    extra_context = {
        'content': content
    }
    
    return render_ace_editor(context, extra_context=extra_context, **kwargs)
    

@register.tag('with_ace_editor')
def with_ace_editor_tag(parser, token):
    """
    Examples:

        {% load djangocms_ace_tags %}

        {% with_ace_editor %}
        console.log("Hello World");
        {% endwith_ace_editor %}

        {% with_ace_editor config=config.ace_config theme="ace/theme/solarized_light" %}
        console.log("Hello World");
        {% endwith_ace_editor %}
    """

    bits = token.split_contents()
    remaining_bits = bits[1:]
    opts = token_kwargs(remaining_bits, parser, support_legacy=True)
    nodelist = parser.parse(('endwith_ace_editor',))
    parser.delete_first_token()
    return AceEditorNode(nodelist, opts)
