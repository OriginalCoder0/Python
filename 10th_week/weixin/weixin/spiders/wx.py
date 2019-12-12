# -*- coding: utf-8 -*-
import scrapy
from weixin.items import WxItem


class WxSpider(scrapy.Spider):
    name = 'wx'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/weixin?type=2&query=python&ie=utf8&s_from=input']

    def parse(self, response):

    	# 获取所有的文章信息
        ullist = response.selector.css("ul.news-list li")
        # 遍历文章
        for li in ullist:
        	item = WxItem()
        	item['title'] = ul.css("h3 a").re_first("<a.*?>(.*?)</a>")
