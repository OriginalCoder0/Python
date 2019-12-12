# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class CsdnSlaveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 要求内容：课程标题，课时、讲师、适合人群、学习人数、价格、课程大纲

    title      = scrapy.Field()  # 标题
    hours      = scrapy.Field()  # 课时长度
    teacher    = scrapy.Field()  # 讲师
    people     = scrapy.Field()  # 适合人群
    number     = scrapy.Field()  # 参加人数
    price      = scrapy.Field()  # 价格
    desciption = scrapy.Field()  # 介绍

"""
class CsdnLoader(ItemLoader):
    # 对redis loader的设置

    default_item_class = CsdnSlaveItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
"""