from urllib import request, parse
import json


def tanslate(keyword):
    ''' urllib 有道翻译 '''
    # 请求地址
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 请求数据
    data = {
        'i': keyword,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1535883818201',
        'sign': 'b8a390c1d6979bd4ddfe3a83048d4dd0',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    # 编码
    data = parse.urlencode(data)
    # 头信息
    headers = {
        'Content-Length': len(data)
    }
    # 发起请求
    try:
        req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=headers)
        res = request.urlopen(req)
        res_json = res.read().decode('utf-8')
        dic = json.loads(res_json)
        print('翻译结果：' + dic['translateResult'][0][0]['tgt'])
    except Exception as e:
        if hasattr(e, 'code'):
            print("访问地址出错")
        else:
            print("其他错误" + str(e))


if __name__ == '__main__':
    print("\n（ 有道翻译 urllib 版，退出请输入 q ）\n")
    while True:
        keyword = input("想翻译啥：")
        if keyword != "q":
            tanslate(keyword)
        else:
            print("Bye-bye")
            break
