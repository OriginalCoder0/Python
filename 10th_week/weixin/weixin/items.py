# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'wx'

    title = scrapy.Field()
    content = scrapy.Field()
    nickname = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()

