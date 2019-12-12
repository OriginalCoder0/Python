def div(dividend, divisor):
    try:
        quotient = dividend/divisor
        return quotient
    except ZeroDivisionError:
        print("除数不能为零啊，哥！")

print("div(4,2) => %d" %(div(4,2)))
print("div(4,0) => %d" %(div(4,0)))
