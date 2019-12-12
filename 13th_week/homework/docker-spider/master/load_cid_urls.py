"""
  手动执行最大和最小用户ID号，遍历并写入Redis中
"""

import redis

def main():

    min_cid = 1
    #max_cid = 23377
    max_cid = 23441

    # 指定Redis数据库信息
    rd = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

    count = 0

    # 遍历用户ID号数据
    for cid in range(min_cid, max_cid+1):
        # 将用户ID和URL写入到Redis中
        if rd.sadd("aobag:cid", str(cid)):
            url = "https://www.aobag.com/customer?cid={}".format(cid)
            rd.lpush("aobag:start_urls", url)
            count = count+1

    print("共计写入cid：%d个"%(count))

#主程序入口
if __name__ == '__main__':
    main()
