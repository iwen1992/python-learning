import re
from urllib import request
class Cbg():
    url='https://n.cbg.163.com/cbg/query.py?serverid=1&act=search_role'
    root_html = '<section>*?class="goodsw">(.*?)</section>'
    a_pattern = '<td><a.*?href="(.+)".*?>(.*?)</a></td>'
    abtn_pattern = '<a href="(.+)" class="goodslist-btn btn btn_red j_buy">购买</a>'
    def __getHtmlSource(self):
        r = request.urlopen(Cbg.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls
    def __getUrl(self,htmls):
        a = re.findall(Cbg.a_pattern,htmls)
        abtn= re.findall(Cbg.abtn_pattern,htmls)
        print(abtn)
        urlArr = []
        trArr = []
        for ahref in a:
            uri={'uri':ahref[0]}
            urlArr.append(uri)
        for relUrl in abtn:
            print(relUrl)
        print(urlArr)
    def get(self):
        htmls = self.__getHtmlSource()
        self.__getUrl(htmls)
cbg = Cbg()
cbg.get()


