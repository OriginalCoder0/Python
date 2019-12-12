# -*- coding: utf-8 -*-
import scrapy, re 
from aobag.items import CustomerItem
from scrapy_redis.spiders import RedisSpider


class BookSpider(RedisSpider):
    name = 'aobag_customer'
    #allowed_domains = ['book.douban.com']
    #start_urls = ['http://book.douban.com/']

    redis_key = "aobag:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(BookSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        
        print("======================",response.status)
        item = CustomerItem()
        ao = response.css(".w-customer")

        # ID号
        #item['cid'] = ao.re_first('<dt><a href="https://www.aobag.com/customer?cid=([0-9]+)">')
        item['cid'] = ao.css('dl > dt a::attr(href)').re_first('http.*?cid=([0-9]+)')

        # 帖子数量
        #item['bbs'] = ao.re_first('<td><span>帖子</span><a .*?>([0-9]+)</a></td>')
        item['bbs'] = ao.css('dl table tr td').re_first('<span>帖子</span><a .*?>([0-9]+)</a>')

        # 用户名
        item['name'] = ao.css("dl h2::text").extract_first()

        # 总重量（小数）
        #item['weight'] = ao.re_first('<td><span>重量</span>([0-9]+)kg</td>')
        #item['weight'] = ao.css('dl table tr td').re_first('<span>重量</span>([0-9]+([.]{1}[0-9]+){0,1})kg')
        item['weight'] = ao.css('dl table tr td').re_first('<span>重量</span>(\d+\.\d+)kg')

        # 总收益（小数）
        #item['profit'] = ao.re_first('<td><span>收益</span>￥([0-9]+)</td>')
        #item['profit'] = ao.css('dl table tr td').re_first('<span>收益</span>￥([0-9]+)')
        item['profit'] = ao.css('dl table tr td').re_first('<span>收益</span>￥(\d+\.\d+)')

        # 余额（小数），余额为零的没有超链接
        #item['balance'] = ao.re_first('<td><span>余额</span><a .*?>￥([0-9]+)</a></td>')
        #item['balance'] = ao.css('dl table tr td').re_first('<span>余额</span>.*?￥([0-9]+).*?')
        item['balance'] = ao.css('dl table tr td').re_first('<span>余额</span>￥(\d+\.\d+)')

        # 购袋数量
        #item['bag_count'] = ao.re_first('<td><span>购袋</span>([0-9]+)</td>')
        item['bag_count'] = ao.css('dl table tr td').re_first('<span>购袋</span>([0-9]+)')

        # 总投递次数
        item['all_deliver'] = ao.css('div > table tr th[colspan="2"] b').re_first('([0-9]+)')

        devliver = ao.css('div > table tr td b::text').extract()

        # 正确投递次数
        item['good_deliver'] = devliver[0]

        # 不当投递次数
        item['bad_deliver'] = devliver[1]

        print(item)
        yield item
