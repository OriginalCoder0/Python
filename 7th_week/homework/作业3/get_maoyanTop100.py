from urllib import request, error
import re, time, os, json

txt_file = "result.txt"
csv_file = "result.csv"

def getPage(url):
    ''' 爬取指定url页面信息 '''
    try:
        #定义请求头信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        }
        # 封装请求对象
        req = request.Request(url,headers=headers)
        # 执行爬取
        res = request.urlopen(req)
        #判断响应状态,并响应爬取内容
        if res.code == 200:
            return res.read().decode("utf-8")
        else:
            return None
    except error.URLError:
        return None


def parsePage(html):
    ''' 解析爬取网页中的内容，并返回字段结果 '''
    #定义解析正则表达式
    pat = '<i class="board-index board-index-[0-9]+">([0-9]+)</i>.*?<img data-src="(.*?)" alt="(.*?)" class="board-img" />.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">([0-9\.]+)</i><i class="fraction">([0-9]+)</i>'
    #执行解析
    items = re.findall(pat, html, re.S)
    #遍历封装数据并返回
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time':  item[4].strip()[5:],
            'score': item[5] + item[6],
        }


def writeFile(content):
    ''' 执行文件追加写操作 '''
    #print(content)
    with open(txt_file,'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False


def main(offset):
    ''' 主程序函数，负责调度执行爬虫处理 '''
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    print(url)

    html = getPage(url)
    #判断是否爬取到数据，并调用解析函数
    if html:
        for item in parsePage(html):
            writeFile(item)


# 判断当前执行是否为主程序运行，并遍历调用主函数爬取数据
if __name__ == '__main__':
    # 删除原来的文件
    if os.path.exists(txt_file):
        os.remove(txt_file)

    for i in range(10):
        main(offset=i*10)
        time.sleep(0.5)

