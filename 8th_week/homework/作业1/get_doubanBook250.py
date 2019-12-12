"""

  豆瓣图书Top250信息爬取

  1. XPath
  2. BeautifulSoup
  3. PyQuery

"""

import requests
from requests.exceptions import RequestException
import os, time, json, re
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery

# https://book.douban.com/top250?start=0
# https://book.douban.com/top250?start=25


txt_file = "doubanBook250.txt"


def getPage(index):
    """ 爬取指定页面 """

    url = "https://book.douban.com/top250"

    data = {
        'start':index,
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }

    try:
        res = requests.get(url, headers=headers, params=data)
        if res.status_code == 200:
            html = res.content.decode('utf-8')
            return html
        else:
            return None
    except RequestException:
        return None


def parsePage(which, content):
    """ 解析网页内容 """

    if which == '1': # 使用XPath解析网页内容
        print("parsePage_xpath")

        html = etree.HTML(content)

        items = html.xpath("//table/tr[@class='item']")

        for item in items:
            yield {
                #'index' : item
                'title' : item.xpath(".//div[@class='pl2']/a/@title")[0],
                'image' : item.xpath(".//img/@src")[0],
                'author': item.xpath(".//p[@class='pl']/text()")[0],
                'score' : item.xpath(".//span[@class='rating_nums']/text()")[0],
            }

    elif which == '2': # 使用BeautifulSoup解析网页内容
        print("parsePage_bs4")

        soup = BeautifulSoup(content, 'lxml')

        items = soup.find_all(name='tr', attrs={'class':'item'})

        for item in items:
            yield {
                #'index' : item
                'title' : item.select("div.pl2 a")[0]['title'],
                'image' : item.find(name='img').attrs['src'],
                'author': item.select("p.pl")[0].get_text(),
                'score' : item.select("span.rating_nums")[0].string,
            }

    elif which == '3': # 使用PyQuery解析网页内容
        print("parsePage_pyquery")

        doc = PyQuery(content)

        items = doc("tr.item")

        for item in items.items():
            yield {
                #'index' :
                'title' : item.find("div.pl2 a").attr('title'),
                'image' : item.find("img").attr('src'),
                'author': item.find("p.pl").text(),
                'score' : item.find("span.rating_nums").text(),
            }


def storeData(content):
    """ 存储解析得到的数据 """

    with open(txt_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(which):
    """ 主程序，负责调度执行爬虫任务 """

    for page in range(0, 10):

        index = page*25
        html = getPage(index)

        if not html:
            print("出错")
            break

        subIndex = 0
        for item in parsePage(which, html):
            subIndex = subIndex+1
            item['index'] = str(index+subIndex)
            print("序号：" + item['index'])
            print("书名：" + item['title'])
            print("封面：" + item['image'])
            print("作者：" + item['author'])
            print("评分：" + item['score'])
            print('-'*32)
            storeData(item)

        time.sleep(0.5)


if __name__ == '__main__':
    if os.path.exists(txt_file):
        os.remove(txt_file)

    print("\n 豆瓣图书Top250信息爬取 \n")
    print(" 1. XPath\n 2. BeautifulSoup\n 3. PyQuery\n")
    which = input(" 请选择解析方式：")
    if re.match(r'^[123]$', which):
        print(" go...")
        main(which)
        print("\n File saved in ./%s" %(txt_file))
    else:
        print(" Sorry！输入不合法")

