import requests
from lxml import etree
import time
url = 'http://www.paoshuzw.com/1/1602/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
hostUrl = 'http://www.paoshuzw.com'
htmlSouce = requests.get(url,headers=header)
htmlSouce.encoding='utf-8'
htmls = htmlSouce.text
eHtml = etree.HTML(htmls)
xPath = '//*[@id="list"]/dl/dd/a'
result = eHtml.xpath(xPath)
for resultI in result:
    radioUrl = hostUrl + resultI.xpath('./@href')[0]
    readHtmlSouce = requests.get(radioUrl,headers=header)
    readHtmlSouce.encoding='utf-8'
    readHtml = readHtmlSouce.text
    rEHtml = etree.HTML(readHtml)
    content = rEHtml.xpath('//*[@id="content"]/text()')
    title = rEHtml.xpath('//*[@class="bookname"]/h1/text()')
    print(title,content)
    try:
        with open('book/quanzhi/%s.txt' % title[0], 'w', encoding='utf-8') as f:
            for items in content:
                f.write(items)
    except Exception as e:
        pass
    print('<%s>下载完毕！'%title)
    time.sleep(1)


