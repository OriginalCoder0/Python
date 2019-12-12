"""
 面向对象编程
"""


class Cat:

    name = ""

    def __init__(self, name):
        print("Initialize Cat")
        self.name = name

    def __del__(self):
        print("Delete Cat")

    def getName(self):
        return self.name


def sayHello():
    """
        Calls sayHello() you will get a hello string.
    """
    print("Hello, World")


cat = Cat('little')
print("The cat's name: ", cat.getName())
print("The cat's name: ", cat.name)

#help(sayHello)
