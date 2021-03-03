import os
import time
#1、os.name系统的名字window-nt
#2、environ环境变量
#3、sep 分隔符 pathsep 路径分隔符 linesep 换行分割分
print(os.linesep)
#二、文件和目录操作
os.mkdir('stddemo')#当前目录下创建stddemo
os.rmdir('stddemo')#删除目录
print(os.getcwd())#打印当前目录
#三、path模块
#os.path.isabs(path)判断path是否为绝对路径
#os.path.getsize(file) 拿到文件的大小
file = os.getcwd()+'\osPro.py'
print(os.path.isabs(file) )
size = os.path.getsize(file)
print(size)