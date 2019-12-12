#使用requests加pyquery爬取所有豆瓣图书标签信息，并将信息储存于redis中

import requests
from pyquery import PyQuery as pq
import redis

def main():
    #使用requests爬取所有豆瓣图书标签信息
    #url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
    url = "https://book.douban.com/tag/"

    proxy = '118.81.64.191:35302'
    proxies = {'http':'http://'+proxy, 'https':'https://'+proxy,}

    #res = requests.get(url, proxies=proxies)
    res = requests.get(url)
    print("status:%d" % res.status_code)
    html = res.content.decode('utf-8')

    # 使用Pyquery解析HTML文档
    #print(html)
    doc = pq(html)
    #获取网页中所有豆瓣图书标签链接信息
    items = doc("table.tagCol tr td a")

    # 指定Redis数据库信息
    link = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    #遍历封装数据并返回
    for a in items.items():
        #拼装tag的url地址信息
        tag = a.attr.href
        #将信息以tag:start_urls写入到Redis中
        link.lpush("book:tag_urls",tag)

    print("共计写入tag：%d个"%(len(items)))

#主程序入口
if __name__ == '__main__':
    main()
