#!/usr/bin/python

import jinja2

from jinja2 import Template

templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

templateVars = {
    "license_info": "This site is released under the GNU General Public License",
    "title": "Toulibre rulez"
    }

templateIndex = templateEnv.get_template( "index.html" )
with open('index.html', 'w') as f:
    f.write( templateIndex.render( templateVars ) )

templateNews = templateEnv.get_template( "news.html" )
with open('news.html', 'w') as f:
    f.write( templateNews.render( templateVars ) )




