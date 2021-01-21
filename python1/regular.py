import re
a = "C|C++|Java|C#|Python|Javascript"
#print(a.index("Python")>-1)
#print("Python" in a)
#Python字符串是否在a中返回['Python']
res = re.findall('Python',a)
if len(res) > 0:
    print("字符串中包含Python")
else:
    print("字符串中没有Python") 

b="12kkad3dasf4da9"
#\d[0-9]所有的数字 \D[^0-9]所有非数字
#\w[a-zA-Z0-9_]
#\s空白字符 \S非空白字符
#re.findall("[a-z]{3,6}",arr)从a中取出a-z的字符，字段长度为3-6个 贪婪模式 re.findall("[a-z]{3,6}?",arr) 非贪婪只会取出a-z 3位不可能取出6位
#*匹配0次或无限多次
#+匹配1次或无限多次
#？匹配0次或1次
#.匹配除换行符外的所有字符
res1 = re.findall("\d",b)
#找寻所有的数字
#返回结果[1,2,3,4,9]
print(res1)
s="acc,abc,afc,acf,ahc"
r2=re.findall("a[c,f]c",s)
#寻找acc，afc的元素
print(r2)
lanuage="PythonC#JavaPHP"
r=re.sub("C#","GO",lanuage)
#sub替换PythonGOJavaPHP
print(r)
lanuage=lanuage.replace("C#","GO")
#replace替换PythonGOJavaPHP
print(lanuage)
#sub第二个参数为函数时value.group()得到符合的值
STRI="A8BDJK201LL2"
def conver(value):
    matched = value.group()
    if int(matched) >= 6:
        return "9"
    else:
        return "0"
res2=re.sub("/d",conver,STRI)
print(res2) 
SITII="A8JSAKDKA828AD"
res3=re.match("\d",SITII)
#返回None匹配第一个字符串，
print(res3)
res4=re.match("\d",SITII)
#8 返回寻找到的第一个
print(res4)
#返回life和python中间的值
TEXT="life is short,i use python"
res4=re.search("life(.*)python",TEXT)
print(r.group(1))
#返回中间值和全部值
print(r.group(0,1))
#返回中间所有的值
print(r.groups())
#返回 is short,i use
res5=re.findall("life(.*)python",TEXT)
print(r)


