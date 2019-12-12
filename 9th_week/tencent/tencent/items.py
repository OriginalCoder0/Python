# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HrItem(scrapy.Item):
	"""
	人事招聘信息封装类
	"""

	# 表名
	table = "hr"

	jid         = scrapy.Field() # 职位id号
	title       = scrapy.Field() # 职位名称
	location    = scrapy.Field() # 工作地点
	jtype       = scrapy.Field() # 类别
	number      = scrapy.Field() # 人数
	duty        = scrapy.Field() # 职责
	requirement = scrapy.Field() # 要求
