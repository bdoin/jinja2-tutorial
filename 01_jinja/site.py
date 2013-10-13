#!/usr/bin/python

import jinja2

from jinja2 import Template
template = Template('Hello {{ name }}!')
print template.render(name='Toulibre')


