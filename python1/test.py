import re
a = '￥7888.00'
res = int(float(re.compile(r'(?<=￥)\d+\.?\d*').findall(a)[0]))
print(res)
print(type(res))