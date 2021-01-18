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
res1 = re.findall("\d",b)
#找寻所有的数字
#返回结果[1,2,3,4,9]
print(res1)
s="acc,abc,afc,acf,ahc"
r2=re.findall("a[c,f]c",s)
#寻找acc，afc的元素
print(r2)