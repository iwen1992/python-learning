# a = 1.313254
# print(round(a,2))
def addNum(a,b):
    result = a+b
    return result
addNum(1,2)
def damages(leave1,leave2):
    damages1 = leave1 * 2
    damages2 = leave2 * 3 + 10
    return damages1,damages2 
resulut = damages(2,3)
#序列解包
skil1,skil2 = damages(2,3)
print(resulut)
print(resulut[0],resulut[1])
print(skil1)
print(skil2)
#序列解包的由来
a,b,c = 1,2,3
d = 1,2,3
a,b,c = d