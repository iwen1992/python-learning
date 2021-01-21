#参数分为1、必须参数 2、关键字参数
def add(x,y):
    result = x + y
    return result
#必须参数    
res = add(1,2)
#关键字参数
a=add(y=1,x=2)

print(res)   
#默认参数 
#默认参数后面不能加必须参数
def classMate(name,age="18",sex="男",school="南昌一中"):
    print("我叫"+name)
    print("今年"+str(age)+"岁")
    print("我是"+str(sex)+"生")
    print("我在"+school+"上学")
classMate("李四","18","男","南昌一中")   
print("~~~~~~~~~~~~")
classMate("张三")