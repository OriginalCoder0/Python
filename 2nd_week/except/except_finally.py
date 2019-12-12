def f1():
    try:
        print(1)
        return 2
    except:
        print(0)
    finally:
        print(3)
        #return 4

print(f1())

print("-"*24)

def f2():
    try:
        print(1)
        #return 2
    except:
        print(0)
        return(0)
    else:
        print(3)
        return 4
    #finally:
        #print(5)
        #return 6

print(f2())
x = 9
