# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AobagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CustomerItem(scrapy.Item):
    # define the fields for your item here like:
    cid     = scrapy.Field() # ID号
    bbs     = scrapy.Field() # 帖子数量
    name    = scrapy.Field() # 用户名
    weight  = scrapy.Field() # 总重量
    profit  = scrapy.Field() # 总收益
    balance = scrapy.Field() # 余额
    bag_count = scrapy.Field() # 购袋数量
    all_deliver  = scrapy.Field() # 总投递次数
    good_deliver = scrapy.Field() # 正确投递次数
    bad_deliver  = scrapy.Field() # 不当投递次数
    