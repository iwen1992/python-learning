class Human():
    sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print("这个人的名字是"+self.name)    