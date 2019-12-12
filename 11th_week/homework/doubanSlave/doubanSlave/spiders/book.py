# -*- coding: utf-8 -*-
import scrapy, re 
from doubanSlave.items import BookItem
from scrapy_redis.spiders import RedisSpider


class BookSpider(RedisSpider):
    name = 'slave_book'
    #allowed_domains = ['book.douban.com']
    #start_urls = ['http://book.douban.com/']

    redis_key = "bookspider:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(BookSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        
        print("======================",response.status)
        item = BookItem()
        vo = response.css("#wrapper")

        item['id']    = vo.re_first('id="collect_form_([0-9]+)"') # ID号
        item['title'] = vo.css("h1 span::text").extract_first()   # 书名

        # 使用正则获取里面的info里面的图书信息
        info = vo.css("#info").extract_first()
        #print(info)

        authors = re.search('<span.*?作者.*?</span>(.*?)<br>',info,re.S).group(1)
        item['author']   = "、".join(re.findall('<a.*?>(.*?)</a>',authors,re.S)) #作者
        item['press']    = " ".join(re.findall('<span.*?出版社:</span>\s*(.*?)<br>',info)) #出版社
        item['original'] = " ".join(re.findall('<span.*?原作名:</span>\s*(.*?)<br>',info)) #原作名
        yz = re.search('<span.*?译者.*?</span>(.*?)<br>',info,re.S)
        if yz:
            item['translator'] = "、".join(re.findall('<a.*?>(.*?)</a>',yz.group(1),re.S)) #译者
        else:
            item['translator'] = ""
        item['imprint'] = re.search('<span.*?出版年:</span>\s*(.*?)<br>',info).group(1) #出版年
        item['pages']   = re.search('<span.*?页数:</span>\s*([0-9]+)<br>',info).group(1) #页数
        item['price']   = re.search('<span.*?定价:</span>.*?([0-9\.]+)元?<br>',info).group(1) #定价
        item['binding'] = " ".join(re.findall('<span.*?装帧:</span>\s*(.*?)<br>',info,re.S)) #装帧
        item['series']  = " ".join(re.findall('<span.*?丛书:</span>.*?<a .*?>(.*?)</a><br>',info,re.S)) #丛书
        item['isbn']    = re.search('<span.*?ISBN:</span>\s*([0-9]+)<br>',info).group(1) #ISBN

        item['score']   = vo.css("strong.rating_num::text").extract_first().strip() #评分
        item['number']  = vo.css("a.rating_people span::text").extract_first() #评论人数
        #print(item)
        yield item
