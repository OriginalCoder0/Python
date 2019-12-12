# -*- coding: utf-8 -*-
import scrapy
from doubanMaster.items import DoubanMasterItem 
from scrapy import Request
from urllib.parse import quote
import redis, re, time, random


class BookSpider(scrapy.Spider):
    name = 'master_book'
    allowed_domains = ['book.douban.com']
    #start_urls = ['http://book.douban.com/']
    base_url = 'http://book.douban.com/'


    def start_requests(self):
        ''' 从redis中获取，并爬取标签对应的网页信息 '''

        r = redis.Redis(host=self.settings.get("REDIS_HOST"), port=self.settings.get("REDIS_PORT"), decode_responses=True)
        
        # 循环爬取每一个标签的图书信息
        while r.llen('book:tag_urls'):
            tag = r.lpop('book:tag_urls')
            # 构造不同标签的url
            url = self.base_url + quote(tag)
            print('='*64)
            print(url)
            yield Request(url=url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        ''' 解析每页的图书详情的url地址信息 '''

        print(response.url)
        lists = response.css('#subject_list ul li.subject-item a.nbg::attr(href)').extract()
        if lists:
            for url in lists:
                item = DoubanMasterItem()
                item['url'] = url
                yield item

        # 获取下一页的url地址
        next_url = response.css("span.next a::attr(href)").extract_first()
        # 判断若不是最后一页
        if next_url:
            url = response.urljoin(next_url)
            # 爬取同一个标签中的下一页图书信息
            yield scrapy.Request(url=url, callback=self.parse)
