'''
 Name: 统计指定目录的大小
 Author: 卢华东
 Date: 2018-06-18
'''

import os

# 自定义统计目录大小函数
def stat_dir_size(dir_path):
    '''
    功能: 统计目录大小
    参数: 指定目录路径
    返回：目录总大小（字节），错误返回-1
    '''
    total = 0

    if os.path.isdir(dir_path):
        dlist = os.listdir(dir_path)
        for f in dlist:
            subdir = os.path.join(dir_path, f)
            if os.path.isfile(subdir):
                total = total + os.path.getsize(subdir)
            if os.path.isdir(subdir):
                total = total + stat_dir_size(subdir)
        return total

    elif os.path.isfile(dir_path):
        return os.path.getsize(dir_path)
    else:
        return -1
    
# 测试
path = input("请输入目录：")
size = stat_dir_size(path)
if size == -1:
    print("(Error) \"{}\" is not a directory.".format(path))
else:
    print("目录大小：", size, "Bytes")

