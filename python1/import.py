#import引入某个文件
#as后面可以简化引入的写法
#如果没有as 那么取C则为modules.importAssort.c
import modules.importAssort as this
print(this.c)
#from ... impot ...
#from ... import *可以引入所有，不推荐使用 
#当使用*号导入所有而在importAssort.py文件里写了
#__all__=["a","c"]则*只被认为是a和c
from modules.importAssort import c
print(c)
from modules.importAssort import *
#importAssort定义了__all__=["a","c"]目前暴露的只有a,c,b将报错
print(a)
# print(b)
print(c)
#引入所需的变量
from modules.importAssort import a,b,c
print(a)
print(b)
print(c)
#导入文件会执行文件并且只会执行一次