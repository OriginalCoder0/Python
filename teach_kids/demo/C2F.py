def f(Ce):
    F = 1.8 * Ce + 32
    return F

x = float(input("请输入摄氏温度值："))
y = f(x)
print("对应的华氏温度值为：", y)
