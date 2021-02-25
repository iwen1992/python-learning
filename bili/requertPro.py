import requests
url = "http://www.dianping.com"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
res = requests.get(url,headers=header)
#print(res.headers)
res.encoding="UTF-8";
html = res.text
print(res.status_code)#status_code为403时表示识别到了爬虫，添加headers请求头，伪装成浏览器访问
print(str(html))