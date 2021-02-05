#第一步需求分析/明确目的
#找到数据对应的网页
#找到数据所在的标签位置
#模拟http请求，向服务器发送这个请求，获得服务器返回给我们的html
#用正则提取所需要的数据
#断点调试 f10 f5 f11 f1
#<li class="course-card-item--v3 js-course-card-item course-card-item--pkg" data-report-position="4"></li>
#<div class="item-line item-line--bottom"></div>
#<span class="line-cell item-price  custom-string">¥877.22</span>
#<span class="line-cell item-user custom-string">0人购买</span>
import re
from urllib import request

class Example():
    url = "https://ke.qq.com/course/list/uniapp?page=1"
    root_pattern='<li class="course-card-item--v3 js-course-card-item [\s\S]*?">([\s\S]*?)</li>'
    price_pattern ='<span class="line-cell item-price  custom-string">([\s\S]*?)</span>'
    custom_pattern = '<span class="line-cell item-user custom-string">([\s\S]*?)</span>'
    name_pattern = '<a href="[/s/S]*?" target="_blank" class="item-tt-link js-course-name" data-hit="[/s/S]*?" cors-name="course" title="[/s/S]*?">([/s/S]*?)</a>'
    url_pattern = '<a href="([\s\S*?])" target="_blank" class="item-img-link [\s\S]*?"'
    def __fetch_content(self):
        r = request.urlopen(Example.url);
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls
    def __analysis(self,htmls):
        roothtml = re.findall(Example.root_pattern,htmls)
        anchorList = []
        for html in roothtml:
            price = re.findall(Example.price_pattern,html)
            custom = re.findall(Example.custom_pattern,html)
            uri = re.findall(Example.url_pattern,html)
            name = re.findall(Example.name_pattern,html)
            anchor = {"name":name,"price":price,"custom":custom,"uri":uri}
            anchorList.append(anchor)
        return anchorList
    def __refine(self,anchorList):
        l = lambda anchor:{
            "price":anchor['price'],
            "custom":anchor['custom'],
            "uri":anchor['uri'],
            'name':anchor['name']
            }
        return map(l,anchorList)   

    def go(self):
        htmls = self.__fetch_content()    
        anchorList = self.__analysis(htmls)
        anchorLists = self.__refine(anchorList)
        print(list(anchorLists))
example = Example()
example.go()             


