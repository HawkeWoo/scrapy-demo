# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 16:21
# @Author  : Hulk Wu
# @File    : run.py


from scrapy import cmdline

name = 'douban_books'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
