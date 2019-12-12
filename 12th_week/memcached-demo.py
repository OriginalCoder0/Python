import pymysql
import memcache


def get_data():
    """ Memcache + MySQL 获取数据 """

    mc = memcache.Client(['127.0.0.1:11211'])

    cachekey = 'product_list'
    res = mc.get(cachekey)
    if res is not None:
        return res

    print('正在查询数据库...')

    conn = pymysql.connect(host='localhost', user='root', password='', db='doubandb', charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from books limit 3'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # 有效时间60秒
    mc.set(cachekey, data, 60)

    return data

print(get_data())

