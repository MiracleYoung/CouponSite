# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from app.conf.gconf import CouponConfig


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    collection = CouponConfig.MONGO_COLLECTION
    mongo_uri = CouponConfig.MONGO_URI
    mongo_db = CouponConfig.MONGO_DB

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item
