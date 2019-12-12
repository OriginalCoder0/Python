#将Redis中的Item信息遍历写入到数据库中
import json
import redis
import pymysql

def main():

    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    # 指定MySQL数据库信息
    db = pymysql.connect(host="localhost",user="root",password="",db="doubandb",charset="utf8")
    #使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["slave_book:items"])

        if data:
            print("***")
            print(source)
        else:
            print("没有了")
            break

        try:
            item = json.loads(data.decode('utf-8'))
            #组装sql语句
            dd = dict(item)
            keys = ','.join(dd.keys())
            values=','.join(['%s']*len(dd))
            sql = "insert into books(%s) values(%s)"%(keys,values)
            #指定参数，并执行sql添加
            cursor.execute(sql,tuple(dd.values()))
            #事务提交
            db.commit()
            print("写入信息成功：",dd['id'])
        except Exception as err:
            #事务回滚
            db.rollback()
            print("SQL执行错误，原因：",err)

#主程序入口
if __name__ == '__main__':
    main()
