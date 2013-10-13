
VERSION = 12.11

#ALL_LINGUAS = cs el es gd lt pt_BR sl hu de fr sr gl pl sk ta ru th bg da zh_TW lv nn sv
ALL_LINGUAS = fr

POFILES=$(shell LINGUAS="$(ALL_LINGUAS)"; for lang in $$LINGUAS; do printf "locale/$$lang/LC_MESSAGES/messages.po "; done)

CATALOGS=$(shell LINGUAS="$(ALL_LINGUAS)"; for lang in $$LINGUAS; do printf "locale/$$lang/LC_MESSAGES/messages.mo  "; done)

sources = \
	site.py \
	template/base.html \
	template/index.html \
	template/news.html \
	template/onenews.html \
	template/social.html

i18_sources = site.py \
	template/index.html

all : $(POFILES) locale/messages.pot $(sources)
	linguas="$(ALL_LINGUAS)"; \
	for lang in $$linguas; do \
	  if test locale/$$lang/LC_MESSAGES/messages.po -nt locale/$$lang/LC_MESSAGES/messages.mo; then \
	    pybabel compile -d locale -l $$lang -i locale/$$lang/LC_MESSAGES/messages.po; \
	  fi; \
	  ./site.py $$lang; \
	done; \
	./site.py en

extract : $(i18_sources)
	pybabel extract -F babel.cfg -o locale/messages.pot ./

update : $(POFILES) locale/messages.pot $(sources)
	linguas="$(ALL_LINGUAS)"; \
	for lang in $$linguas; do \
	  if test locale/messages.pot -nt locale/$$lang/LC_MESSAGES/messages.po; then \
	    pybabel update -d locale -l $$lang -i locale/messages.pot; \
	  fi; \
	done;


clean:
	rm -f *.html *.pyc
