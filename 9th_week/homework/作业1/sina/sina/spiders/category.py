# -*- coding: utf-8 -*-
import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):

        dlist = response.selector.css("div.section")
        print('='*64)

        for div in dlist:
            # 获取一级标题
            tit01 = div.xpath(".//h2[@class='tit01']/text()").extract()
            #tit01 = div.css("h2.tit01::text").extract()
            tit01s = ''
            for t in tit01:
                tit01s = tit01s + t
            print(tit01s)
            #print(div.re("<h2 class=\"tit01\".*?>(.*?)</h2>")[0])

            # 获取二级标题
            ddlist = div.xpath("./div")
            for tt in ddlist:
                tit02 = tt.xpath(".//h3[@class='tit02']/a/text()|.//h3[@class='tit02']/span/text()|.//h3[@class='tit02']/text()").extract_first()
                print("  |—— %s"%(tit02))
                #tit02 = div.css("h3.tit02 a::text").extract()

                # 获取三级标题
                tit03 = tt.xpath(".//ul[@class='list01']/li/a/text()").extract()
                for ttt in tit03:
                    print("      |—— %s"%(ttt))

            print("")
            # end of for loop

        print('='*64)
