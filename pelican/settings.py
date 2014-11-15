#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ted Lawless'
SITENAME = u'Ted Lawless'
SITEURL = 'https://lawlesst.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_SAVE_AS = '{slug}/index.html'


#Turn off tags
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

FEED_RSS = 'feed.rss'

THEME = './themes/simple-bootstrap'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

#ARTICLE_PATHS = ['notebook']
ARTICLE_URL = 'notebook/{slug}.html'
ARTICLE_SAVE_AS = 'notebook/{slug}.html'
