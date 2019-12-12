# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class TencentPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
	def __init__(self, host, user, password, database, port):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.port = int(port)

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host = crawler.settings.get("MYSQL_HOST"),
			user = crawler.settings.get("MYSQL_USER"),
			password = crawler.settings.get("MYSQL_PASS"),
			database = crawler.settings.get("MYSQL_DATABASE"),
			port = crawler.settings.get("MYSQL_PORT"),
		)

	def open_spider(self, spider):
		""" 负责连接数据库 """
		print('*'*64)
		print("%s, %s, %s, %s, %s"%(self.host, self.user, self.password, self.database, self.port))
		#self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset="utf8", port=self.port)
		self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset="utf8", port=self.port)
		print(self.db)
		self.cursor = self.db.cursor()

	def process_item(self, item, spider):
		""" 执行数据表的写入操作 """

		data = dict(item)
		keys = ','.join(data.keys())
		values = ','.join(['%s']*len(data)) # 得到的形式是 '%s,%s,%s'
		sql = "insert into %s(%s) values(%s)"%(item.table, keys, values)

		# 真正把value放到sql语句
		self.cursor.execute(sql, tuple(data.values()))
		self.db.commit()
		return item

	def close_spider(self, spider):
		""" 关闭连接数据库 """

		print('/'*64)
		self.db.close()
