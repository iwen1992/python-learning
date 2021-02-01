from functools import reduce
#lambda匿名函数
#lambda函数内部不能赋值
f=lambda x,y:x+y
# print(f(1,2))
#map类 map(func,list)
list_x=[1,2,3,4,5,6,7,8]
def square(x):
    return x*x
res=map(square,list_x);
print(list(res))
#map可以传入多个列表
#如果多个列表长度不一样执行到最短的列表完之后不再执行
list_y=[1,2,3,4,5,6]
list_z=[1,2,3,4,5,6]
r=map(lambda x,y:x*x+y,list_y,list_z)
print(list(r))
#reduce 连续计算 第三个参数，插入list最前面
#(((((1+2)+3)+4)+5)+6)
#前两个数的结果+第三个数
r2=reduce(lambda x,y:x+y,list_y);
print(r2)
#filter过滤 filter(func,list)
list_q=[0,1,2]
r3=filter(lambda x : True if x==1 else False,list_q)
print(list(r3))
