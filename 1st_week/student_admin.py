'''
 Name: 学员信息管理系统
 Athor: 卢华东
 Date: 2018-06-18
 Description: 数据临时存放在变量列表中，实现学生信息的添加、
              删除和查询操作
'''

# 学员信息列表
stulist = [
        {'name':'Allen','age':20,'classid':'Python02'},
        {'name':'Bonus','age':20,'classid':'Python03'},
        {'name':'Carrie','age':20,'classid':'Python04'}]

# 显示学员信息列表
def showStu(stulist):
    '''
    '''
    if len(stulist) == 0:
        print("(I) No Data from Stu")
        return
    print("|{0:<5} | {1:<10} | {2:<5} | {3:<10}".format("sid",
        "name","age","classid"))
    print("-"*40)
    for i in range(len(stulist)):
        print("|{0:<5} | {1:<10} | {2:<5} | {3:<10}".format(i+1,
            stulist[i]['name'],stulist[i]['age'],stulist[i]['classid']))
    print("")

# 初始化界面
def showMainPage():

    print("="*12, "学员信息在线管理", "="*12)
    print("{0:1} {1:13} {2:15}".format(" ", "1.查看学员信息", 
        "2.添加学员信息"))
    print("{0:1} {1:13} {2:15}".format(" ", "3.删除学员信息", 
        "4.退出系统"))
    print("="*42)


# 开始啦
while True:
    showMainPage()
    key = input("请输入对应的选择：")
    if key == "1":
        print("="*14, "学员信息浏览", "="*14)
        showStu(stulist)
        input("按回车键继续：")
    elif key == "2":
        print("="*14, "学员信息添加", "="*14)
        stu = {}
        stu['name'] = input("请输入要添加的姓名：")
        stu['age'] = input("请输入要添加的年龄：")
        stu['classid'] = input("请输入要添加的班级号：")
        stulist.append(stu)
        print("(I) 添加成功")
        input("按回车键继续：")
    elif key == "3":
        print("="*14, "学员信息删除", "="*14)
        sid = input("请输入你要删除的信息id号：")
        if int(sid) > 0 and int(sid) <= len(stulist):
            del stulist[int(sid)-1]
            print("(I) 删除成功")
        else:
            print("(E) 删除失败")
        input("按回车键继续：")
    elif key == "4":
        print("="*18, "再见", "="*18)
        break
    else:
        print("Try again!")

