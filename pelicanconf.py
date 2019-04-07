#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kishored'
SITENAME = 'attetta'
SITEURL = 'https://attetta.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('Xing', 'https://www.xing.com/profile/KrishnaKishore_Donthikurthi/'),
#          ('Github', 'https://github.com/kcodek'),)          




DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Tell pelican which folder to output to. 
# By default it will be generated to blog/source/output but we wanted them to appear in blog/output instead.
OUTPUT_PATH='../output'


# Tell Pelican where it can find the custom theme
THEME = 'theme/elegant'

# Tell Pelican where the plugins folder is located 
PLUGIN_PATHS = ['plugins/', ]

# A typical Pelican website will utilize many different plugins to extend its capabilities. Each plugin must be setup individually within pelicanconf.py. 
# The PLUGINS variable contains all plugins being used by the website. 
PLUGINS = ['i18n_subsites', 'tipue_search', 'sitemap' ]

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))  

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# The i18n_subsites plugin relies on a language called Jinja2. 
# To properly configure the i18n_subsites plugin we must also add the JINJA_ENVIRONMENT variable 
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# choose a css from pelican-bootstrap3 theme - theme/static/css/ 
BOOTSTRAP_THEME = 'flatly'

#  Pelican displays code blocks using the Pygments code highlighter.
PYGMENTS_STYLE = 'monokai'

# we must tell Pelican where to look for the static media files 
STATIC_PATHS = ['img', 'pdf']

# We have the option to define where Pelican should look for our blog's pages. 
# By default Pelican expects them to be in the content/pages folder. 
# It is not necessary to state the path but it is a good practice to do so. 
PAGE_PATHS = ['pages']

#To change the URL to show the content type and date as well. 
# The ARTICLE_URL variable states what should display in the web browser's address bar 
# while the ARTICLE_SAVE_AS variable defines where the article being generated should be output to.

# ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

#For pages, categories, and tags. 
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# CATEGORY_URL = 'category/{slug}'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'categories.html'

# TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags.html'


# The CNAME file is now added the local repository. 
# This creates another issue: when we generate the website in Pelican the output folder gets deleted before it is loaded with new files. We need to create an exception for CNAME to avoid this. 
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['CNAME']