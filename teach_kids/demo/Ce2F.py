"""
 文件：Ce2F.py
 描述：将摄氏温度转换为华氏温度
"""

C = input("请输入摄氏温度值：")

if C.isdigit():
    F = 1.8 * float(C) + 32
    print("对应的华氏温度为：{:.2f}".format(F))
else:
    print("你输入的不是数字！")
