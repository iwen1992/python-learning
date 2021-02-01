import time
def decorator(func):
    def warpper():

        print(time.time())
        func()
    return warpper
@decorator
def f2():
    print("this is 装饰器")
f2()            
    