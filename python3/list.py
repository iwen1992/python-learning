#列表推导式
#for in 前面加操作
a = [1,2,3,4,5,6,7,8]
b = [i*i for i in a]
print(b)

x = [1,2,3,4,5,6,7,8]
y = [i*i for i in x if i<=5]
print(y)
#set tuple都能使用列表推导式
c = {1,2,3,4,5,6,7,8}
d = {i*i for i in c if i<=5}
print(d)

students = {
    "张三":18,
    "李四":15,
    "王五":10
}
student = [key for key,value in students.items()]
print(student)