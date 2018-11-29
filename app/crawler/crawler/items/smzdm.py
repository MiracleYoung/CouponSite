#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/29/18

__author__ = 'MiracleYoung'

import scrapy


class BaiCaiJiaItem(scrapy.Item):
    title = scrapy.Field()
    discount = scrapy.Field()
    user = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    info = scrapy.Field()



