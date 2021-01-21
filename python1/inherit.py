from classHuman import Human
#子类Inherit继承Human
#一般一个子类只能继承一个父类
#python可以一个子类继承多个父类
#单继承的好处是关系明了、清晰
class Inherit(Human):
    #因为父类有name,age所以需要吧name,age传给父类
    def __init__(self,school,name,age):
        self.school=school
        #类调用实例函数，普通方法调用并不会触发类的机制自动补齐self
        #实例化对象调用则不需要传入self
        #可行并不推荐，如果改变了父类将会需要更改所有父类的名字
        #super()代替父类
        #Human.__init__(self,name,age)
        super(Inherit,self).__init__(name,age)
    def get_age(self):
        print(self.age)
        #子类方法可以和父类方法同名，同名时调用的是子类的函数
        #super()函数可以用在子类的另一函数里
    def get_name(self):
        super(Inherit,self).get_name()
        print("这是子类getname方法")    
inherit = Inherit("江南小学","小明","19")
print(inherit.sum)
print(inherit.name)
print(inherit.age) 
inherit.get_name()

#实例化对象调用和类调用，类调用需要传入self
#在其他函数中类是不能调用函数的
inherit.get_age() 
Inherit.get_age()      

