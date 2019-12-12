# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class DangdangPipeline(object):
    '''处理item的类'''

    def process_item(self, item, spider):
        '''
        处理爬取数据，如果爬取的书名没有，就把这条记录剔除。
        :param item: 爬虫item类
        :param spider: 爬虫超类
        :return: 剔除条目或者item
        '''
        if item['name'] == None:
            raise DropItem("Drop item found: %s" % item)
        else:
            return item


class MysqlPipeline(object):
    '''处理item写入数据库的类'''

    def __init__(self, host, database, user, password, port):
        '''
        构造类，创建全局变量
        :param host: 数据库主机路径
        :param database: 数据库名称
        :param user: 数据库用户名
        :param password: 数据库密码
        :param port: 数据库端口
        '''
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db = None
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):
        '''
        类方法，用此方法获取数据库相应信息来连接数据库
        :param crawler: crawler类
        :return: 带有数据库信息的类。在这里调用类构造方法
        '''
        return cls(
            host=crawler.settings.get("MYSQL_HOST"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get("MYSQL_PASS"),
            port=crawler.settings.get("MYSQL_PORT")
        )

    def open_spider(self, spider):
        '''
        通过设置文件里的信息链接到数据库，并准备好游标以便后面使用
        :param spider:
        :return:
        '''
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        '''
        执行插入操作，将item相应信息插入数据库并保存
        :param item: 爬虫item类
        :param spider: spider超类
        :return: 爬虫item类
        '''
        sql = "insert into pythonbook(name,price,pic,author,publisher,comments, pubdate, description) values('%s','%s','%s','%s','%s','%s', '%s', '%s')"%(item['name'],item['price'],item['pic'],item['author'],item['publisher'],item['comments'], item['pubdate'],item['description'])
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def close_spider(self, spider):
        '''
        关闭数据库连接
        '''
        self.db.close()


class ImagePipeline(ImagesPipeline):
    '''处理图像的类'''

    def get_media_requests(self, item, info):
        '''
        从item内拿到图片url信息，创建Request等待调度执行
        :param item: 爬虫item类
        :param info: 消息
        :return: None， yield一个带图片URL的Request
        '''
        yield Request(item['pic'])

    def item_completed(self, results, item, info):
        '''
        下载完成后，如果url不是有效的，就筛选掉这个数据。
        :param results:
        :param item:
        :param info:
        :return: 爬虫item类
        '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")

        return item