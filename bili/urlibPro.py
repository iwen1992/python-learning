from urllib import request
url = "http://www.baidu.com"
#添加header信息反扒措施
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
req = request.Request(url,headers=header)
res = request.urlopen(req)
html = res.read();
html = str(html,encoding='utf-8')
print(str(html))