#python代码最后一行要加一行换行
#比较运算符要加空格
#冒号前面不需要空格
#python代码缩进等于四个空格
username='admin'
password='111111'
print("请输入你的账号")
user_name=input()
print ("请输出你的密码")
user_password=input()
if user_name == username and user_password == password:
    print("success")
else:
    print("fail")    
