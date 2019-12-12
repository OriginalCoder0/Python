'''
 Name: 学员信息管理系统（MySQL版）
 Athor: 卢华东
 Date: 2018-07-04
 Description: 学生信息存储在MySQL数据库中，实现学生信息的添加、
              删除和查询操作。
              stu_info_system.sql 是原始的数据库文件，操作之前
              请将其导入到您的数据库。
'''

import sys
import pymysql
import datetime
import time

class Stu_ops:

    # 定义属性
    __table = ''

    # 定义方法
    # 构造方法
    def __init__(self, user, passwd, db, host='localhost', port=3306):
        """
            Parameter 'db' is the database which you want to connect.
        """
        # 记录操作日志
        self.__log = open(".student_mysql_%d.log"%(time.time()), 'w')
        self.__record("== Log - Student Information Management System ==", False)
        self.__record(" + %s" %time.asctime(time.localtime(time.time())), False)

        try:
            # type(db): pymysql.connections.Connection, if connect failed, Null
            self.__db = pymysql.connect(host=host, user=user, password=passwd, db=db, charset='utf8')
            self.__cursor = self.__db.cursor()
            what  = self.query("SELECT VERSION()", log=False)
            where = self.query("SELECT DATABASE()", log=False)
            who   = self.query("SELECT USER()", log=False)
            self.__record(" + %s\n + %s\n + %s\n" %(what[0][0], where[0][0], who[0][0]), False)
        except Exception as err:
            self.__record("Can not connected to %s, reason: %s" %(db, err))
            self.__record("Exit ...\n")
            #exit(1)
            sys.exit()


    # 析构方法
    def __del__(self):
        """
            Disconnect database safely.
        """
        try:
            self.__db.close()

        except:
            print("(E) No pymysql.connections.Connection object")
            print("(I) I'm sorry about that, please check PyMySQL connect args")
            print("(I) For more details, see %s\n" %(self.__log.name))

        finally:
            self.__log.close()



    # 日志记录
    def __record(self, log, timestamp=True, newline=True):

        if newline == True:
            nc = '\n'
        else:
            nc = ''

        if timestamp == True:
            self.__log.write("[%f] %s%s" %(time.time(), log, nc))
        else:
            self.__log.write("%s%s" %(log, nc))

    # 获取日志文件名
    def getLogName(self):
        return self.__log.name


    # 设置数据表
    def setTable(self, table):
        self.__table = table


    # 执行SQL语句并提交事务
    def query(self, sql, log=True):

        if log == True:
            self.__record("SQL: \"%s\"" %(sql))

        try:
            ret = self.__cursor.execute(sql)
            # 事务提交
            self.__db.commit()
            if log == True:
                self.__record("Query OK, %d rows affected" %(ret))
            return self.__cursor.fetchall()
        except Exception as err:
            # 如果异常则回滚
            self.__db.rollback()
            if log == True:
                self.__record("Query Failed, reason: %s" %(err))
            return None


    # 查询方法
    def findAll(self):
        self.__record(">>> findAll()")
        qlist = self.query("SELECT * FROM %s" %(self.__table))
        if qlist == None:
            print("The %s table has no data" %(self.__table))
            return -1
        else:
            #print("-"*56)
            print("+"+"-"*10+"+"+"-"*10+"+"+"-"*10+"+"+"-"*5+"+"+"-"*10+"+")
            print("|{0:<10}|{1:<10}|{2:<10}|{3:<5}|{4:<10}|".format(" ID"," Name"," Gender"," Age"," Class"))
            print("+"+"-"*10+"+"+"-"*10+"+"+"-"*10+"+"+"-"*5+"+"+"-"*10+"+")
            for row in qlist:
                # MySQL保存出生日期的类型是date，所以这里需要将datetime.date转换成str类型
                # 然后换算成年龄
                #birthdate = row[3].strftime("%Y-%m-%d")
                birthyear = row[3].strftime("%Y")
                now = time.localtime()
                age = int(now.tm_year) - int(birthyear)
                print("|{0:>10}|{1:>10}|{2:>10}|{3:>5}|{4:>10}|".format(row[0],row[1],row[2],age,row[4]))
                """
                for item in row:
                    print("|{0:<10}".format(item), end="")
                print("|")
                """
            print("+"+"-"*10+"+"+"-"*10+"+"+"-"*10+"+"+"-"*5+"+"+"-"*10+"+")
            return 0


    # 删除方法
    def delete(self, sid):
        self.__record(">>> delete(id)")
        ret = self.query("DELETE FROM %s WHERE sid=%s" %(self.__table, str(sid)))
        if ret == None:
            return -1
        else:
            return 0


    # 添加方法
    def insert(self, data):
        self.__record(">>> insert(data)")
        ret = self.query("INSERT INTO %s values(%d,'%s','%s','%s','%s')"
                %(self.__table, data[0], data[1], data[2], data[3], data[4]))
        if ret == None:
            return -1
        else:
            return 0


    # 测试用的
    def test(self):
        #pass
        print("Hello Stu_ops")


# 初始化界面
def showMainPage():

    print("="*12, "学员信息在线管理", "="*12)
    print("{0:1} {1:13} {2:15}".format(" ", "1.查看学员信息",
        "2.添加学员信息"))
    print("{0:1} {1:13} {2:15}".format(" ", "3.删除学员信息",
        "4.退出系统"))
    print("="*42)


def main():

    # 实例化
    stu = Stu_ops(user='root', passwd='******', db='stu_info_system')
    stu.setTable('student_info')
    #stu.test()

    while True:
        showMainPage()
        key = input("请输入对应的选择：")
        print("")
        if key == "1":
            print("="*14, "学员信息浏览", "="*14)
            ret = stu.findAll()
            if ret == 0:
                print("(I) 查询成功")
            else:
                print("(E) 查询失败")

        elif key == "2":
            print("="*14, "学员信息添加", "="*14)
            data = list()
            sid       = input("请输入学号 (eg. 201807001): ")
            name      = input("请输入姓名 (must!): ")
            gender    = input("请输入性别 (male|female|unknown): ")
            birthdate = input("请输入出生日期 (eg. 1999-01-01): ")
            classid   = input("请输入班级 (eg. Python07): ")
            data.append(int(sid))
            data.append(name)
            data.append(gender)
            data.append(birthdate)
            data.append(classid)

            ret = stu.insert(data)
            if ret == 0:
                print("(I) 添加成功")
            else:
                print("(E) 添加失败")

        elif key == "3":
            print("="*14, "学员信息删除", "="*14)
            sid = input("请输入你要删除的信息id号：")
            ret = stu.delete(int(sid))
            if ret == 0:
                print("(I) 删除成功")
            else:
                print("(E) 删除失败")

        elif key == "4":
            print("="*18, "再见", "="*18)
            print("您可以查看日志：%s\n" %(stu.getLogName()))
            break
        else:
            print("Try again!")

        input("按回车键继续 -> ")
        print("")


if __name__ == "__main__":
    main()

