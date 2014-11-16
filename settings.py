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


DEFAULT_DATE_FORMAT = ('%m/%d/%Y')

TWITTER_USERNAME = 'tedlawless'

DEFAULT_PAGINATION = False

FEED_RSS = 'feed.rss'

THEME = './themes/just-read'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

#ARTICLE_PATHS = ['notebook']
ARTICLE_URL = 'notebook/{slug}.html'
ARTICLE_SAVE_AS = 'notebook/{slug}.html'

PAGE_SAVE_AS =  '{slug}/index.html'

DISQUS_SITENAME = 'tedlawlessnotebook'
GOOGLE_ANALYTICS = 'UA-2790298-5'
SOCIAL = (
	('github', 'http://github.com/lawlesst', 'Github'),
	('twitter', 'http://twitter.com/tedlawless', 'Twitter'),
	('stack-overflow', 'http://stackoverflow.com/users/758157/lawlesst', 'Stack Overflow')
)

#MD_EXTENSIONS = (['toc', 'footnotes'])

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc']


LOAD_CONTENT_CACHE = False