# -*- coding: utf-8 -*-
import scrapy
from tencent.items import HrItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=2196&keywords=python']

    def parse(self, response):
        """ 解析当前招聘列表信息的url地址 """

        print('+'*64)
        detailUrls = response.css('tr.even a::attr(href),tr.odd a::attr(href)').extract()
        # 遍历url地址
        for url in detailUrls:
        	# 构建绝对的url地址（域名加相对地址）
        	fullUrl = response.urljoin(url)
        	print(fullUrl)
        	yield scrapy.Request(url=fullUrl, callback=self.parse_page)

        print('-'*64)
        # 获取下一页的url地址
        nextUrl = response.css('#next::attr(href)').extract_first()
        if nextUrl != "javascript:;":
        	url = response.urljoin(nextUrl)
        	yield scrapy.Request(url=url, callback=self.parse)

    def parse_page(self, response):
    	""" 解析详情页 """

    	item = HrItem()

    	item["jid"] = response.selector.re_first('onclick="applyPosition\(([0-9]+)\);"')
    	item["title"] = response.css('#sharetitle::text').extract_first()
    	item["location"] = response.selector.re_first('<td><span class="lightblue l2">工作地点：</span>(.*?)</td>')
    	item["jtype"] = response.selector.re_first('<td><span class="lightblue">职位类别：</span>(.*?)</td>')
    	item["number"] = response.selector.re_first('<td><span class="lightblue">招聘人数：</span>([0-9]+)人</td>')
    	duty = response.xpath('//table//tr[3]//li/text()').extract()
    	item["duty"] = ''.join(duty)
    	requirement = response.xpath('//table//tr[4]//li/text()').extract()
    	item["requirement"] = ''.join(requirement)

    	#print(item)
    	yield item

