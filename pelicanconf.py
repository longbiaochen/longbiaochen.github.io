#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Meta info
SITENAME = u"Felix's Blog"
SITESUBTITLE = u"The world's mine oyster."
AUTHOR = u'Felix Chan'
# SITEURL = 'http://longbiaochen.com'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
THEME = "theme/notmyidea"

# Publishing
# WITH_FUTURE_DATES = False # Do not publish articles set in the future
DELETE_OUTPUT_DIRECTORY = True
# TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'files', 'codes', 'extra/CNAME', 'extra/README',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/README': {'path': 'README'},'extra/proxy.pac': {'path': 'proxy.pac'},}
# PAGE_EXCLUDES=('about-me.html',)

# Plugins
PLUGIN_PATHS = ['./pelican-plugins/',]
<<<<<<< HEAD
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.include_code']
=======
# PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.include_code']
>>>>>>> b79d871b344a0ed69f40e017d4da2d13f23c37a0

# Feeds
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False
POST_LIMIT = 9999

# Disqus
DISQUS_SITENAME = 'longbiaochen'

# # Social widget
# SOCIAL = (
# 			('新浪微博', 'http://t.cn/longbiaochen'),
# 		  	('QQ空间', 'http://qzone.qq.com/longbiaochen'),
# 		  	('Twitter', 'http://twitter.com/longbiaochen'),
# 		  	('Facebook', 'http://facebook.com/longbiaochen'),
# 		  	('Linkedin', 'http://linkedin.com/longbiaochen'),			  		  		  
# 		 )
