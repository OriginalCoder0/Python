num = input("请输入一个数字：")

print(num.isdigit())

if isinstance(eval(num), int):
    print("这是一个整数")
elif isinstance(eval(num), float):
    print("这是一个小数")
else:
    print("啥都不是")
