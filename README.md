## djangocms-ace
[![Build Status](https://travis-ci.org/TigerND/djangocms-ace.svg?branch=master)](https://travis-ci.org/TigerND/djangocms-ace)

Ace Editor plugin for Django CMS.

### Installation

This plugin requires `Django CMS` 3.2 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-ace``.
* Add ``'djangocms_ace'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_ace``.

### Some Examples

```html
{% load djangocms_ace_tags %}

{% with_ace_editor %}
  console.log("Hello World");
{% endwith_ace_editor %}

{% with_ace_editor config=config.ace_config theme="ace/theme/solarized_light" %}
  console.log("Hello World");
{% endwith_ace_editor %}
```

or as a single tag:

```html
{% load djangocms_ace_tags %}

{% ace_editor content='console.log("Hello World");' %}

{% ace_editor config=config.ace_config content='console.log("Hello World");' %}

{% ace_editor config=config.ace_config theme="ace/theme/solarized_light" content='console.log("Hello World");' %}
```

```html
{% for item in object_list %}
  {% ace_editor content=item.content|safe %}
{% endfor %}
```

### License

The MIT License (MIT)
