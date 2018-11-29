#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/29/18

__author__ = 'MiracleYoung'

import scrapy


class TestSpider(scrapy.spiders.Spider):
    name = 'tb-test'
    start_urls = ["https://www.taobao.com/", ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response=response,
            formdata={
                'TPL_username': '13916227150',
                'TPL_password': ',Yql0723,',
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        print(response)
