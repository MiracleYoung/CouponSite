#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/6/18

__author__ = 'MiracleYoung'

from scrapy import Request
from scrapy.spiders import Spider
from ..items import DoubanItem


class DoubanSpider(Spider):
    name = 'douban'
    # start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url=url, headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/em/text()').extract()[0]
            item['movie'] = movie.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            item['score_num'] = movie.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]/text()').extract()[0]
            yield item
