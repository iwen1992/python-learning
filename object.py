#类 = 面向对象
#类  对象==》封装，继承，多态
#class名字首字母大写
class Student():
    #类变量
    name="张三"
    age=11
    #__init__()构造函数，实例变量
    #self实例函数本身
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def do_homework(self):
        print("name" + str(self.name))
        print("age" + str(self.age))
student = Student("李四","28")
student.do_homework() 
studentTwo = Student("张三","18")
studentTwo.do_homework()
print(Student.name)
print(Student.age)
#__dict__所有的实例变量成员
print(student.__dict__)
class classMate():
    name = "小明"
    age = 18
    def __init__(self,name,age):
        print(self.name)
        self.name = name
        self.age = age
        print(age,name)
        
classMateOne = classMate("小红","21")        
