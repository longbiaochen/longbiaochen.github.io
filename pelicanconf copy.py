#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Felix Chan'
SITENAME = u"Felix's Blog"
SITESUBTITLE = u"The world's mine oyster."
# SITEURL = 'http://longbiaochen.com'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
THEME = "theme/flat"

STATIC_PATHS = ['images', 'files', 'codes', 'extra/CNAME', 'extra/README',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/README': {'path': 'README'},'extra/proxy.pac': {'path': 'proxy.pac'},}
DELETE_OUTPUT_DIRECTORY = True
# PAGE_EXCLUDES=('about-me.html',)
# Plugins
PLUGIN_PATHS = ['./plugins/',]
PLUGINS = ['sitemap', 'neighbors', 'related_posts', 'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.include_code']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Social widget
SOCIAL = (
			('新浪微博', 'http://t.cn/longbiaochen'),
		  	('QQ空间', 'http://qzone.qq.com/longbiaochen'),
		  	('Twitter', 'http://twitter.com/longbiaochen'),
		  	('Facebook', 'http://facebook.com/longbiaochen'),
		  	('Linkedin', 'http://linkedin.com/longbiaochen'),			  		  		  
		 )
