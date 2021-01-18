class Privatecount():
    name="变量"
    __score="私有变量"
    
    def get_private_count(self):
        result=self.__score
        return(result)
privateCount = Privatecount()
privateCount1 = Privatecount()
privateCount2 = Privatecount()
res = privateCount.get_private_count()
#对象的特征是可以动态添加私有变量的
privateCount2.__score = 1
print(privateCount2.__score)
#动态加上去的私有变量实际上和原有的私有变量不是一个东西
print(res)
#私有变量是不可以在函数外部直接访问的
#python处理私有变量的方法是吧私有变量变成了其他的变量，通过查字典可以看到__score被转换为_privatecount__score
#此时外部直接访问私有变量__score是找不到的
#如果非要去寻找则可以通过_privatecount__score得到
print(Privatecount.__dict__)
print(Privatecount._privatecount__score)
print(PrivateCount1.__score)        