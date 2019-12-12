from urllib.request import urlretrieve
from urllib.parse import urlencode
import os, time, json
import requests

def getPage(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
    except:
        return None


def getImage(json):
    data = json.get("data")
    if data:
        for item in data:
            image_list = item.get("image_list", [])
            title = item.get("title")
            for im in image_list:
                yield {
                    'image':im.get("url"),
                    'title':title,
                }
    pass

def saveImage(item):
    path = os.path.join("./mypic/", item.get('title'))
    if not os.path.exists(path):
        os.mkdir(path)

    local_image_url = item.get("image")
    image_url = "http:"+local_image_url.replace("list","large")
    save_pic = path+"/"+local_image_url.split("/").pop+".jpg"

    urlretrieve(image_url, save_pic)

def main(offset):
    json = getPage(offset)
    for item in getImage(json):
        print(item)
        saveImage(item)


if __name__ == "__main__":
    for i in range(5):
        main(offset=i*20)
        time.sleep(1)
