# -*- coding: utf-8 -*-
import scrapy
import json


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        '''
        人人网登录操作
        使用 yield 与 scrapy 的 FormRequest 提交用户登录信息，并使用回调方法访问 parse 来接下来处理返回的代码。

        注意：测试时请使用您的用户名与密码

        '''

        # 登录页面的 URL
        login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018822125828'

        # 登录的表单信息，其中用户名与密码请自行输入正确值
        data = {
            'email': '15899962704',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'password': '2c18e5058b11daacfa19994395734b2490de52f533def51d9eb68e009710a7b4',
            'rkey': 'a30944a4db9c355ed88accbaeb6263b9',
            'f': 'http%3A%2F%2Fzhibo.renren.com%2Ftop',
        }

        yield scrapy.FormRequest(
            url = login_url,
            formdata = data,
            callback = self.parse
        )

    def parse(self, response):
        '''
        爬虫 start_requests 方法的回调函数。
        返回的是 JSON 数据，解析 response 将数据取出，如果登录失败，显示其中的 failDescription 值。
        如果这个字段不存在，则说明登录成功打印登录成功。

        '''
        res = json.loads(response.text)

        print('='*64)
        print(res)

        # 判断返回的JSON数据中是否存在名为'failDescription'的key
        if 'failDescription' in res:
            print("登录失败，原因是："+res['failDescription'])
        else:
            print("登录成功")
            url = res['homeUrl']
            print("准备跳转到 %s"%(url))

            # 获取主页面
            yield scrapy.Request(url=url, callback=self.parseHome)

        print('='*64)

    def parseHome(self, response):
        """
        登录成功后请求主页面的回调函数
        """
        print('+'*64)
        username = response.selector.css("a.hd-name::text").extract_first()
        print("您好，%s"%(username))

