from bs4 import BeautifulSoup
import requests
url = "http://hc.jiangxi.gov.cn/col/col38268/index.html"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
res = requests.get(url,headers=header)
res.encoding="UTF-8"
html = res.text
print(html)
soup = BeautifulSoup(html)
a = soup.findAll("li")
print(a)
# print(soup)
