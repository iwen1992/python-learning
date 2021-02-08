day = 1
# switcher = {
#     0:'Sunday',
#     1:"Monday",
#     2:'Tuesday'
# }
# ...
# 用字典的方式模拟switch
# ...
def get_Sunday():
    return "Sunday"
def get_Monday():
    return "Monday"
def get_Tuesday():
    return "Tuesday"
def get_Default():
    return "unknow"  
switcher = {
    0:get_Sunday,
    1:get_Monday,
    2:get_Tuesday
}
          
# day_name = switcher.get(day,"unkown")#get 如果字典里面没这项则返回unkown
day_name = switcher.get(day,get_Default)()
print(day_name)