# 闭包
# 闭包=函数+环境变量，不受函数外部变量影像
def curve_pre():
    a=25
    def curve(x):
        return a*x*x
    return curve
f = curve_pre()
a=100
result=f(2)
print(result) 
# 非闭包
# 闭包必须要引用外部的变量才能形成闭包
def f1():
    # 全局变量
    f1a=10
    def f2():
        # f1a局部变量
        f1a=20
        print(f1a)
    #step1 10
    print(f1a)
    #step2 执行f2 20
    f2()
    #step3 全局变量被打印 10
    print(f1a)
f1()  
#非闭包方式 累加
origin = 0
def go(step):
    #若想在函数内部对函数外的变量进行操作 global
    global origin
    new_pos = origin + step
    # python认为如果左边出现的变量为局部变量，并不会向上寻找
    origin = new_pos
    return new_pos
print(go(2))  
print(go(3)) 
print(go(6))
# 闭包方式 累加
# 不改变全局变量
originS = 0
def factory(pos):
    def goStep(step):
        #声明pos不是本地变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return goStep
torist = factory(originS)
print(torist(2))     
print(torist(3))   
print(torist(5))     


