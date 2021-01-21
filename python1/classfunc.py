class addFunc():
    name="类方法"
    methed="@classmethod"
    num1=1
    #私有变量
    __score=0
    def __init__(self,methed,name):
        self.methed=methed
        self.name=name
        self.score=0
    #双下划綫__私有方法不可在外部调用    
    def making(self,score):
        if score < 0:
            self.score = 0
            
        else:
            self.score = score
        print(self.score)           

    @classmethod
    def plus_num(cls):
        cls.num1 += 1
        print(cls.num1)
    @staticmethod
    def add(x,y):
        result = x+y
        return result    
addfunc = addFunc("测试类方法","测试类方法")
addfunc.plus_num()
res = addfunc.add(1,2)   
print(res)
addfunc.making(-1)


