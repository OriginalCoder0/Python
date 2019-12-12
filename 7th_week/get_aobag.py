from urllib import request, error
import re
import os, time

home_title = 'aobag.com-新分类 新回收'
url = "https://www.aobag.com/customer?cid="

# max_cid@20180910 = 18745
# max_cid@20180910 = 18750
# max_cid@20180911 = 18939
# max_cid@20180912 = 19163
# max_cid@20180913 = 19271
# max_cid@20180916 = 20021
# max_cid@20180917 = 20092
# max_cid@20180918 = 20190
# max_cid@20180919 = 20306
# max_cid@20180920 = 20396
# max_cid@20180921 = 20468
# max_cid@20180922 = 20570
# max_cid@20180923 = 20672
# max_cid@20180924 = 20885
# max_cid@20180925 = 20977
# max_cid@20180926 = 21120
# max_cid@20180929 = 21483
# max_cid@20180930 = 21519
# max_cid@20181001 = 21602
# max_cid@20181002 = 21694
# max_cid@20181003 = 21736
# max_cid@20181004 = 21808
# max_cid@20181005 = 21877
# max_cid@20181006 = 21915
# max_cid@20181007 = 21948
# max_cid@20181008 = 22057
# max_cid@20181009 = 22217
# max_cid@20181010 = 22293
# max_cid@20181011 = 22373
# max_cid@20181014 = 22534
# max_cid@20181014 = 22704
# max_cid@20181019 = 22840
# max_cid@20181022 = 22960
# max_cid@20181023 = 23154
# max_cid@20181024 = 23210
# max_cid@20181026 = 23288
# max_cid@20181027 = 23312
# max_cid@20181107 = 23686
# max_cid@20181111 = 23865
# max_cid@20181114 = 24231
# max_cid@20181116 = 24353
# max_cid@20181117 = 24365
# max_cid@20181118 = 24413
# max_cid@20181119 = 24473
# max_cid@20181122 = 24683
# max_cid@20181123 = 24762
# max_cid@20181125 = 24780 before 我是未来
# max_cid@20181125 = 25035 after 我是未来
# max_cid@20181126 = 25192
# max_cid@20181127 = 25351
# max_cid@20181128 = 25422
# max_cid@20181130 = 25628
# max_cid@20181205 = 26090
# max_cid@20181209 = 26294
# max_cid@20181211 = 26405
# max_cid@20181215 = 26749
# max_cid@20181218 = 26984
# max_cid@20181218 = 27255

def getTitle(cid):
    req = request.Request(url + str(cid))

    try:
        res = request.urlopen(req)
        html = res.read().decode("utf-8")

        #print(len(html))
        title = re.findall("<title>(.*?)</title>", html)
        #print(title[0])
        return title[0]
    except error.HTTPError as e:
        print(e.reason)
        print(e.code)
        return None
    except error.URLError as e:
        print(e.reason)
        return None


if __name__ == '__main__':
    print("Go ...")
    cid = 27255

    #for cid in range(188, 288):
    while True:
        result = getTitle(cid)
        if result == home_title:
            print("最大ID号：%d"%(cid))
            break
        elif result == None:
            print("出错")
            break
        else:
            print(str(cid) + ' : ' + result)

        cid = cid + 1

        time.sleep(1)

    print("ok")
