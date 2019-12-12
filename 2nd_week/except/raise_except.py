
def func(num):
    if num < 1:
        raise Exception("Invalid level!", num)


try:
    func(0)
except Exception as err:
    print("No: %s"%(err))

