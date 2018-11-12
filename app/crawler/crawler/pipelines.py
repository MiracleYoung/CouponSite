# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from app.etc.conf import config


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline:
    collection = config.MONGO_COLLECTION
    mongodb_uri = config.MONGO_URI
    db = config.MONGO_DB

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item
