# -*- coding: utf-8 -*-
import scrapy
from demo.items import FangItem


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.5i5j.com']
    #start_urls = ['http://fang.5i5j.com/']
    start_urls = ['https://fang.5i5j.com/bj/loupan/']

    def parse(self, response):
        hlist = response.css("div.houseList_list")
        for vo in hlist:
            item = FangItem()
            item['title']   = vo.css("h3.fontS20 a::text").extract_first()
            item['address'] = vo.css("span.addressName::text").extract_first()
            item['time']    = vo.re("<span>(.*?)开盘</span>")[0]
            item['clicks']  = vo.re("<span><i>([0-9]+)</i>浏览</span>")[0]
            item['price']   = vo.css("i.fontS24::text").extract_first()

            yield item
