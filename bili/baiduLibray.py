import re
import requests
from lxml import etree
#requests.get() 和 requests.session.get()区别在于一个不携带状态一个携带状态
session = requests.session()
def fetch_url(url):
    #https://wenku.baidu.com/robots.txt
    header = {
        'User-agent': 'Baiduspider'
    }
    return  session.get(url).content.decode('utf-8')
    #return requests.get(url,headers=header).text
def get_docId(url):
    return re.findall('view/(.*?).html',url)[0]
def get_docType(htmlSouce):
    return re.findall(r"doc_info.*?\:(.*?)\,\"cover_list\"",htmlSouce)
def main():
    url = input("请输入你要下载的文档地址")
    htmlSouce = fetch_url(url)
    docId = get_docId(url)
    docType = get_docType(htmlSouce)
    print(htmlSouce)
    print(docType)
main()
#https://wenku.baidu.com/view/54dbf3caae1ffc4ffe4733687e21af45b207fed4.html?fr=search-1-income7-score_2-psrec1&fixfr=5MtIF%2FgDHaIPARbB8R4Mhg%3D%3D