a = ["apple","orange","banner","pig"]
for x in a:
    print(x)
b= [["a","b","c","d"],(1,2,3)]
for y in b:
    for z in y:
        print(z)
        print(z,end="") 
else:
    print("结束了") 
#break,containue
#直接break掉之后不会执行else

for x in a:
    if x == "orange":
        break
    print(x)
else:
    print("break结束了")      
for x in a:
    if x == "orange":
        continue
    print(x)
else:
    print("continue结束了")     
#for 执行指定次数
#range(0,10)从0开始共10次
#range(0,10,2)从0开始共10次，以2步长分割

for xx in range(0,10):
    print(xx)
for yy in range(0,10,2):
    print(yy)
#步长取值也可以用下面方式  
yyy = [0,1,2,3,4,5,6,7,8,9]
yyyy = yyy[0:len(yyy):2]
print(yyyy)                                 