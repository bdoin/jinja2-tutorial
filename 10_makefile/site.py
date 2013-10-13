#!/usr/bin/python

import jinja2
from jinja2 import Template
import gettext
import sys
import codecs

try:
    locale = sys.argv[1]
except:
    print "Missing locale"
    sys.exit(1)

# Load the proper locale catalog
try:
    t = gettext.translation('messages', 'locale', languages=[locale])
except:
    if locale != "en":
        print "Translation file not found for locale: " + locale
        sys.exit(1)
    t = gettext.NullTranslations()
_ = t.ugettext


templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader,
                                  extensions=['jinja2.ext.i18n'] )
templateEnv.install_gettext_callables(t.ugettext, t.ungettext, newstyle=True)

templateVars = {
    "license_info": _("This site is released under the GNU General Public License"),
    "title": _("Toulibre rulez"),
    "news": [],
    "locale": locale
    }

templateIndex = templateEnv.get_template( "index.html" )
with codecs.open('index-' + locale + '.html', 'w', encoding='utf-8') as f:
    f.write( templateIndex.render( templateVars ) )

# Create the list of news
# In real life we would read the news from a file
# instead of hard coding them here

for i in range(24):
    templateVars['news_title'] = 'news ' + str(i)
    templateVars['news_content'] = 'this is good news'
    templateOneNews = templateEnv.get_template( "onenews.html" )
    templateVars['news'].append( templateOneNews.render( templateVars ) )

templateNews = templateEnv.get_template( "news.html" )
with codecs.open('news-' + locale + '.html', 'w', encoding='utf-8') as f:
    f.write( templateNews.render( templateVars ) )
