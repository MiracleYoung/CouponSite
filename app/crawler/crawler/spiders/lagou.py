#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/6/18

__author__ = 'MiracleYoung'

from scrapy.spiders import Spider


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
