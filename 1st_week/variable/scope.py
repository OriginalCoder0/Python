"""
    变量作用域
"""

g1 = 'one'

def func():
    g1 = 'one piece'
    global g2
    g2 = 'two piece'
    print("In func():", g1)
    print("In func():", g2)

    print("inside : id(g1) = %s" %(id(g1)))
    print("inside : id(g2) = %s" %(id(g2)))

g2 = 'two'
func()
print("g1 = ", g1)
print("g2 = ", g2)

print("outside: id(g1) = %s" %(id(g1)))
print("outside: id(g2) = %s" %(id(g2)))
