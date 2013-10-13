#!/usr/bin/python

import jinja2

from jinja2 import Template

templateLoader = jinja2.FileSystemLoader( searchpath="." )
templateEnv = jinja2.Environment( loader=templateLoader )

templateVars = {
    "license_info": "This site is released under the GNU General Public License",
    "title": "Toulibre rulez"
    }

template = templateEnv.get_template( "test_index.html" )
print template.render( templateVars )



