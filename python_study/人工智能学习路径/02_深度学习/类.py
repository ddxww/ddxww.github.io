class Student:
    def __init__(self,a,b,c,d):
        self.name=a
        self.sex=b
        self.age=c
        self.height=d

    def listen(self):
        print('listen')
    def show(self):
        print('show')
    def foo1(self):
        self.age+=1

stu1=Student('ddd','man',20,180)
print(stu1)
print(type(stu1))
print(stu1.name)
print(Student.listen(stu1))
print(stu1.listen())
print(stu1.show())
stu1.xxx=123
print(stu1.xxx)
del stu1.xxx
print(stu1.age)
stu1.foo1()
print(stu1.age)

