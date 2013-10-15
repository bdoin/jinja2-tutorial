#!/usr/bin/python

import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

templateVars = {
    "license_info": "This site is released under the GNU General Public License",
    "title": "Toulibre rulez",
    "news": []
    }

templateIndex = templateEnv.get_template( "index.html" )
with open('index.html', 'w') as f:
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
with open('news.html', 'w') as f:
    f.write( templateNews.render( templateVars ) )
