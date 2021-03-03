import requests
from lxml import etree #对数据做一个预处理
from urllib import request
import time
url='https://www.huya.com/g/2168'
user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
headers={
    'User_Agent':user_agent
}
res = requests.get(url,headers=headers)
resHtml = res.text
#xPath = '//*[@id="js-live-list"]/li/a[1]/img'
xPath = '//img[@class="pic"]'
#筛选数据
etRes = etree.HTML(resHtml)
xpathRes = etRes.xpath(xPath)
#保存数据
for imgItem in xpathRes:
    img = imgItem.xpath('./@data-original')[0]
    imgName = imgItem.xpath('./@alt')[0]
    try:
        request.urlretrieve(img,'pic/'+imgName+'.jpg')
    except Exception as e:
        pass
    print('<%s>下载完毕！'%imgName)
    time.sleep(1)







