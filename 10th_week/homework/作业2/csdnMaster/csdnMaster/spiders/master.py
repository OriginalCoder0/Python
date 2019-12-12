# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from csdnMaster.items import CsdnMasterItem
from scrapy import Request


class MasterSpider(CrawlSpider):
    ''' 此类继承CrawlSpider，负责主要的爬取功能 '''

    name = 'master'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/k']

    base_url = 'https://edu.csdn.net/courses/k/p'

    rules = (
    	Rule(LinkExtractor(allow=('https://edu.csdn.net/courses/k/p[0-9]+',)), callback='parse_item', follow=True),
    )


    def start_requests(self):
        '''
          爬虫开始方法，通过对页数参数读取，
          在for循环，再通过yield来创建一个Request并访问parse方法
        '''
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = self.base_url+str(page)
            yield Request(url=url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        ''' 对具体爬取数据的操作 '''

        item = CsdnMasterItem()
        itemlist = response.xpath(".//div[@class='course_dl_list']")
        for items in itemlist:
            item['url'] = items.xpath(".//a/@href").extract_first()
            yield item

        