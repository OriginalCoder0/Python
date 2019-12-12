# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JdPipeline(object):

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db  = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ''' 类方法，从settings中获取MongoDB的配置信息 '''

        return cls(mongo_url=crawler.settings.get('MONGO_URL'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        ''' 开启爬虫方法，连接MongoDB '''

        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        ''' 处理item的方法，把item作为字典放入MongoDB的集合内 '''

        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        '''
        爬取完成后关闭爬虫
        :param spider: 爬虫超类
        :return:
        '''
        self.client.close()
