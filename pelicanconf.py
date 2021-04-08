#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'spencer'
SITENAME = 'spewil'
SITEURL = ''

PATH = 'content'
THEME = 'themes/brutalist'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = ''

DIRECT_TEMPLATES = ['index', 'categories', 'tags']
INDEX_SAVE_AS = 'writing.html'  # redirect the index (posts) to a separate page

ARTICLES_PATHS = ['posts']
PAGE_PATHS = ['pages']

# URLs
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('name', 'link'), )

# Social link and icon filepath
# SOCIAL = (('/theme/icons/email.svg', 'mailto:spencer@spewil.com'), )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME'
    },
    'extra/favicon.ico': {
        'path': 'favicon.ico'
    }
}
