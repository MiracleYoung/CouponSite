#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/29/18

__author__ = 'MiracleYoung'

import re, ast

import scrapy

from app.crawler.crawler.items.smzdm import BaiCaiJiaItem


class BaiCaiJiaSpider(scrapy.spiders.Spider):
    name = 'smzdm-baicaijia'
    start_urls = ['https://faxian.smzdm.com/9kuai9/']

    def parse_page_content(self, response):
        for i in response.xpath('//*[@id="feed-main-list"]/li'):
            item = BaiCaiJiaItem()
            item['title'] = i.xpath('div/h5/a/text()').extract()[0].strip()
            item['discount'] = i.xpath('div/div[2]/text()').extract()[0].strip()
            item['user'] = {
                'name': i.xpath('div/div[3]/div[1]/span/a[2]/text()').extract()[0].strip(),
                'homepage': i.xpath('div/div[3]/div[1]/span/a[2]/@href').extract()[0].strip(),
                'avatar': i.xpath('div/div[3]/div[1]/span/a[1]/img/@src').extract()[0].strip(),
            }
            item['content'] = i.xpath('div/div[4]/text()').extract()[0].strip()
            item['link'] = i.xpath('div/div[5]/div[2]/div/div/a/@href').extract()[0].strip()
            item['info'] = i.xpath('div/div[5]/div[2]/div/div/a/@onclick').extract()[0]
            pattern = re.compile(r'gtmAddToCart(?P<info>.*)')
            item['info'] = ast.literal_eval(pattern.match(item['info']).groups()[0])
            print(item)
            yield item

    def parse(self, response):
        # 预读第一页
        self.parse_page_content(response)
        # 获取下一页
        next_page = response.xpath('//*[@id="J_feed_pagenation"]/li[last()]/a/@href')
        if next_page:
            for link in next_page:
                # 如果有下一页回调parse_page_content
                yield scrapy.Request(link.extract(), callback=self.parse_page_content)
