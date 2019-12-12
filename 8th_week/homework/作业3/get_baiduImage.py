"""
  下载指定关键字的百度图片，并保存到本地
"""

from urllib.parse import urlencode
from urllib.request import urlretrieve
import requests
import os, time
import random


def getPage(keyword, offset):
    """
    描述：根据关键字和Ajax加载偏移获取URL内容

    参数：keyword 指定搜索的关键字
          offset  传给pn参数GET提交到服务器

    返回：Json数据对象
    """

    timestamp = int(time.time())
    randomNum = random.randint(100,999)
    appendix = str(timestamp)+str(randomNum)

    data = {
        'tn'        : 'resultjson_com',
        'ipn'       : 'rj',
        'ct'        : '201326592',
        'is'        : '',
        'fp'        : 'result',
        'queryWord' : keyword,
        'cl'        : 2,
        'lm'        : -1,
        'ie'        : 'utf-8',
        'oe'        : 'utf-8',
        'adpicid'   : '',
        'st'        : -1,
        'z'         : '',
        'ic'        : 0,
        'word'      : keyword,
        's'         : '',
        'se'        : '',
        'tab'       : '',
        'width'     : '',
        'height'    : '',
        'face'      : 0,
        'istype'    : 2,
        'qc'        : '',
        'nc'        : 1,
        'fr'        : '',
        'expermode' : '',
        'pn'        : offset,
        'rn'        : 30,
        'gsm'       : hex(offset),
        appendix    : '',
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }

    url = "https://image.baidu.com/search/acjson?" + urlencode(data)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None



def getImage(content):
    """
    描述：从Json数据中获取所需的图片URL

    参数：content 要解析的Json数据

    返回：解析后的字典数据
    """

    data = content.get('data')

    if data:
        for item in data:
            # middleURL 和 thumbURL 都包含图片链接
            image = item.get('middleURL')

            yield {
                'image': image
            }


def storeImage(item, localDir):
    """
    描述：根据图片链接信息将图片下载到本地

    参数：item     包含图片URL的字典数据
          localDir 指定保存的目录

    返回：None
    """

    if not os.path.exists(localDir):
        os.mkdir(localDir)

    #path = os.path.join(localDir + '/', str(time.time()))
    imageURL = item.get('image')

    if imageURL:
        # 文件名使用原来的就好了
        savePath = localDir + '/' + imageURL.split('/').pop()
        urlretrieve(imageURL, savePath)


def main(keyword, page):
    """ 主程序，接收关键字，负责调度爬虫处理 """

    for index in range(0, int(page)):
        content = getPage(keyword, index*30)
        for item in getImage(content):
            print(item)
            storeImage(item, './' + keyword)

        print('-'*12)
        time.sleep(1)

    print("\n图片保存在 './" + keyword + "' 目录")


if __name__ == '__main__':

    print("\n 百度图片-爬虫程序（不输入则默认爬取2页'街拍'） \n")
    keyword = input("请输入关键字：")
    page = input("请输入爬取页数：")

    if keyword and page:
        print("\n 爬取关于“%s”的图片，共%s页...\n"%(keyword, page))
        main(keyword, page)
    else:
        print("\n 默认操作...\n")
        main('街拍', 2)

