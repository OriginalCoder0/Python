"""
  爬取京东商城网址购物车中的所有商品信息

  采用浏览器伪装技术获取京东购物车信息（维持Cookie信息）

  https://cart.jd.com/cart.action
"""

import requests
import re, json
from pyquery import PyQuery


def getCartPage(url):
    """ 获取京东购物车页面 """

    # 封装请求头部信息，cookie是必须的！
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': 0,
        'cookie': '__jdu=15259298350381188491031; shshshfpa=2c79ee6b-6b8e-fef7-4873-efc28d939842-1529295065; shshshfpb=11d5dc743e34146b1a886b83c67e03367168ea2da14b8fd515b2730da8; user-key=86866200-14c7-4745-aea1-99966bb7f952; __jdc=122270672; __jdv=122270672|direct|-|none|-|1536816622941; PCSYCityID=1601; ipLoc-djd=1-72-2799-0; 3AB9D23F7A4B3C9B=QYBDNTPA54B3TGW4TOXFWV6WYCZNCJ6AGLDNZ6NEOUYIZ5TATSG6SNVX5AFKG74OJTTESECXVQZ2ZPOQQJELJH6WSM; ipLocation=%u5317%u4EAC; areaId=1; cart-main=xx; cn=3; cd=0; shshshfp=962a5db897840d6cb9f836d5f497229c; __jda=122270672.15259298350381188491031.1525929835.1536848003.1536887347.8; shshshsID=7b74088241c0b48921e1dfe585e1afcb_1_1536890539558',
        'origin': 'https://cart.jd.com',
        'referer': 'https://cart.jd.com/cart.action',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    print("getting ... %s\n"%url)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        #return res.json()
        html = res.content.decode('utf-8')
        return html
    else:
        return None


def parsePage(content):
    """ 使用PyQuery解析京东购物车页面 """

    doc = PyQuery(content)
    items = doc("div.item-form")

    if items:
        # 获取并返回商品信息
        for item in items.items():

            yield {
                'name' : item.find("div.p-name a").text(),
                'props': item.find("div.props-txt").text(),
                'price': item.find("div.p-price strong").text(),
                'count': item.find("div.quantity-form input").attr('value'),
                'totalPrice': item.find("div.p-sum strong").text(),
                'weight': item.find("div.p-sum span").attr('data'),
            }


def main():
    """ 主程序，负责调度爬虫处理 """

    url = 'https://cart.jd.com/cart.action'
    #url = 'https://cart.jd.com/queryProductService.action?random=0.10704370965957088&t=0'

    content = getCartPage(url)

    for item in parsePage(content):
        print("商品：" + item['name'])
        print("属性：" + item['props'])
        print("单价：" + item['price'])
        print("数量：" + item['count'])
        print("总价：" + item['totalPrice'])
        print("重量：" + item['weight'])
        print('-'*64)


if __name__ == '__main__':
    main()
