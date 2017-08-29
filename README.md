# jinja2-tutorial

A lesson by lesson tutorial of the template engine Jinja2 in Python
with Bootstrap and I18N.

This tutorial was written by Bruno Coudoin for a presentation made
for the Toulibre's LUG in Toulouse France.

## 01\_jinja

My first jinja2 template, all in Python.

## 02\_jinja\_file

Now the template is in a separate file. The python code is used to
load it, execute it to create a text buffer out of it.

## 03\_jinja\_extends

It is possible to create a base template with some parts maked as
'blocks'. Another template can extend it and fill the blocks.

## 04\_bootstrap

Twitter's Bootstrap is an interesting technology to create a responsive
Web site.

## 05\_bootstrap-menu\_active

We can set variables in a template and access them in the base template.

## 06\_bootstrap-column

Bootstrap uses a 12-column layout. It is possible to define how many
columns should be used for a given content and for a given user screen
size.

## 07\_jinja\_loops

We can pass Python list to a Jinja2 template. In a template we can
loop over them.

## 08\_jinja\_import

You can create macros in Jinja2 templates. These can be imported in
other templates and be called anywhere and you can pass them
parameters.

## 09\_jinja\_i18n

We will use pybabel to extract strings marked as `{% trans %}Hello{%
endtrans %}`in Jinja2 templates and strings marked as `_('Hello')` in
the Python code.

## 10\_makefile

We create a Makefile to make it easy to maintain our web site.
