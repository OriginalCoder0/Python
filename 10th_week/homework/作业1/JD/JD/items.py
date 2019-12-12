# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    collection = 'products' # 集合的名字

    title   = scrapy.Field() # 标题
    price   = scrapy.Field() # 价格
    pic     = scrapy.Field() # 图片url
    comment = scrapy.Field() # 评论数
    store   = scrapy.Field() # 商店
