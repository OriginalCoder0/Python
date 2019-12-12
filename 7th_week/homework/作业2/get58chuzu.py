import requests, re, lxml
from bs4 import BeautifulSoup

# 状态维持
s = requests.session()


# 抓取信息
def get58content(pindex):
    '''
        抓取58租房分页信息，并返回必要信息
        参数 pindex：查询页码
        返回 finall_list：结果列表
    '''

    # 定义存储信息列表
    findall_list = []

    try:
        # 发起请求
        url = 'http://bj.58.com/dashanzi/chuzu/pn' + str(pindex) + '/?ClickID=1'
        res = s.get(url).content.decode('utf-8')
        # print(res)

        # soup定义
        soup = BeautifulSoup(res, "lxml")
        dlist = soup.select('.listUl li')

        # 遍历房源ul标签中里li
        for tag in dlist:
            # 标题
            if tag.select(".des h2 a"):
                title = tag.select(".des h2 a")[0].get_text()
                title = str(title).strip()
            else:
                title = ''
            # 图片
            if tag.select(".img_list a img[lazy_src]"):
                pic = tag.select(".img_list a img[lazy_src]")[0].get('lazy_src')
                pic = 'http:' + pic
            else:
                pic = ''
            # 户型
            if tag.select(".des p"):
                roomtype = tag.select(".des p")[0].get_text()
                roomtype = ''.join(re.split(r'\s+', str(roomtype)))
            else:
                roomtype = ''
            # 价格
            if tag.select(".money b"):
                money = tag.select(".money b")[0].get_text() + "元"
            else:
                money = ''
            # 放入字典并添加至结果列表
            dic = {'标题': title, '图片': pic, '户型': roomtype, '价格': money,}
            findall_list.append(dic)

        return findall_list
    except Exception as e:
        if hasattr(e, "code"):
            print("请求出错")
        else:
            print("其他错误" + str(e))


# 主函数
if __name__ == '__main__':
    print("\n （ 抓取58同城大山子租房信息，返回【标题、图片、户型、价格】）\n")

    while True:
        pIndex = input("请输入查询页码：")
        if not re.match('^[1-9][0-9]*$', pIndex):
            print("不合法，请重新输入！")
        else:
            break

    result_list = get58content(pIndex)
    total = len(result_list)

    for i in result_list:
        if i['标题']:
            print("标题："+i['标题'])
            print("户型："+i['户型'])
            print("价格："+i['价格'])
            print("图片："+i['图片']+' \n')
        else:
            # 移除无效数据
            result_list.remove(i)

    print("\n总爬取数：" + str(total) + "，有效数：" + str(len(result_list)))
