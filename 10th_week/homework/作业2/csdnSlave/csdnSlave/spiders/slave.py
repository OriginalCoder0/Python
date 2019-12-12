# -*- coding: utf-8 -*-
import scrapy, re
from csdnSlave.items import CsdnSlaveItem
from scrapy_redis.spiders import RedisSpider


class SlaveSpider(RedisSpider):
    ''' 此类继承RedisSpider，负责主要的爬取功能 '''

    name = 'slave'
    allowed_domains = ['edu.csdn.net']
    #start_urls = ['http://edu.csdn.net/']

    # Redis内的键值对
    redis_key = 'csdnspider:start_urls'


    def __init__(self, *args, **kwargs):
        ''' 初始方法，设置在redis的配置 '''

        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SlaveSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        ''' 爬虫具体数据的处理 '''

        item = CsdnSlaveItem()
        item['title'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/h1/text()").extract_first().strip()  # 标题
        item['hours'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[1]/span[2]/text()").extract_first()  # 课时长度
        item['teacher'] = response.xpath(".//div[@class='professor_name']/a/text()").extract_first()  # 讲师
        item['people'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[2]/span[2]/text()").extract_first()  # 适合人群
        item['number'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[2]/span[3]/span[2]/text()").extract_first()  # 参加人数
        item['price'] = response.xpath(".//div[@class='sale']/span[@class='money']/text()").extract_first().strip()  # 价格
        item['desciption'] = response.xpath(".//div[@class='outlin_discribe']/span/text()").extract_first().strip()  # 介绍

        yield item

