
class People:

    name = ""

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Student(People):
    grade = ""

    def __init__(self, name, grade):
        People.__init__(self, name)
        self.grade = grade

    def getName(self):
        return ("Name:" + self.name)

    def getGrade(self):
        return self.grade

person = People("Rudy")
print(person.getName())
person.name = "Rudy Lo"
print(person.getName())
#print(person.name)

stu = Student("Tina", "A+")
print(stu.getName())
print(stu.getGrade())

