import re
from urllib import request
class Cbg():
    url='https://n.cbg.163.com/cbg/query.py?serverid=1&act=search_role'
    a_pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
    def __getHtmlSource(self):
        r = request.urlopen(Cbg.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls
    def __getUrl(self,htmls):
        a = re.findall(Cbg.a_pattern,htmls)
        urlArr=[]
        for ahref in a:
            uri={'uri':ahref['href']}
            urlArr.append(uri)
        print(urlArr)
    def get(self):
        htmls = self.__getHtmlSource()
        self.__getUrl(htmls)
cbg = Cbg()
cbg.get()


