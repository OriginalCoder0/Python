# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request, Spider
from JD.items import JdItem


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    allowed_domains = ['www.jd.com']
    #start_urls = ['http://www.jd.com/']
    base_url = 'https://list.jd.com/list.html?cat=670,671,672&page='


    def start_requests(self):
        """ 爬虫开始的地方，需要对页数进行处理 """

        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = self.base_url+str(page)
            yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)


    def parse(self, response):
        """ 对Selenium返回的页面进行解析 """

        products = response.xpath("//*[@id='plist']/ul/li")

        for product in products:
            item = JdItem()

            item['title'] = product.xpath(".//div/div[3]/a/em/text()").extract_first().strip()
            item['price'] = product.xpath(".//div/div[2]/strong[1]/i/text()").extract_first()
            item['pic'] = product.xpath(".//div/div[1]/a/img/@src").extract_first()
            item['comment'] = product.xpath(".//div/div[4]/strong/a/text()").extract_first()
            item['store'] = product.xpath(".//div/div[5]/span/a/text()").extract_first()

            yield item


