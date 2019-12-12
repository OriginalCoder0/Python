import requests, json


def tanslate(keyword):
    ''' requests 有道翻译 '''
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

    # 发起请求
    try:
        res = requests.post(url, data=data)
        res_data = res.content.decode('utf-8')
        res_data = json.loads(res_data)
        print('翻译结果：' + res_data['translateResult'][0][0]['tgt'])
    except Exception as e:
        if hasattr(e, 'code'):
            print("访问地址出错")
        else:
            print("其他错误" + str(e))


if __name__ == '__main__':
    print("\n（ 有道翻译 requests 版，退出请输入 q ）\n")
    while True:
        keyword = input("想翻译啥：")
        if keyword != "q":
            tanslate(keyword)
        else:
            print("Bye-bye")
            break