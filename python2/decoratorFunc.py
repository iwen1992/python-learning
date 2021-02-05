import time
def decorator(func):
    #*xxx可变参数
    #**kw可变变量
    def warpper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return warpper
@decorator
def f2():
    print("this is 装饰器")
def f3(test1,test2,test3):
    print("this is "+test1)
    print("this is "+test2)
    print("this is "+test3)

f2() 
f3("h","0","2")           
    