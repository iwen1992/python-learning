from selenium import webdriver
url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6'
options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
options.add_argument("--headless")
brower = webdriver.Chrome("G:\python\python-learning\chromedriver_win32\chromedriver.exe",chrome_options=options)
xPath = '//a[@class="js_song"]'
brower.get(url)
#智能等待 5s内加载完毕即可！5s为最长等待时间
brower.implicitly_wait(5)
srcList = brower.find_elements_by_xpath(xPath)
for src in srcList:
    print(src.get_attribute('href'))



