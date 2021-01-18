#snippet小工具
#加快编码速度
#在python中是严格模式，不同类型1 “1”也是不相等的
print("请输入a的值")
a=input()
print(a)
print(type(a))
print(a == 1)
a=int(a)
if a == 1:
    print("orange")
elif a == 2:
    print("banner")
elif a == 3:
    print("apple")
else:
    print("啥也不是")            
    