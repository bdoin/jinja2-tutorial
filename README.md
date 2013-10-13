jinja2-tutorial
===============

A lesson by lesson tutorial of the template engine Jinja2 in Python
with Bootstrap and I18N.

This tutorial has been written by Bruno Coudoin for a presentation
made for the Toulibre's LUG in Toulouse France.

# 01_jinja

My first jinja2 template, all in Python

# 02_jinja_file

Now the template is in a separate file. The python code is used to
load it, execute it to create a text buffer out of it.

# 03_jinja_extends

It is possible to create a base template with some parts maked as
'blocks'. Another template can extend it and fill the blocks.

# 04_bootstraps

Twitter bootstraps is an interesting technology to create a responsive
Web site.

# 05_bootstrap-menu_active

We can set variables in a template and access them in the base template.

# 06_bootstrap-column

Bootstap uses a 12 columns layout. It is possible to define how many
columns should be used for a given content and for a given user screen
size.

# 07_jinja_loops

We can pass Python list to a Jinja2 template. In a template we can
loop over them.

# 08_jinja_import

You can create macros in Jinja2 templates. These can be imported in
other templates and be called anywhere and you can pass them
parameters.

# 09_jinja_i18n

We will use pybabel to extract strings marked as {% trans %}Hello{%
endtrans %} in Jinja2 templates and strings marked as _('Hello') in
the Python code.

# 10_makefile

We create a Makefile to make it easy to maintain our web site.