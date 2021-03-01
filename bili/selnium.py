from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
# options.add_argument('--proxy-server=http://ip:port')
options.add_argument("--headless")
driver = webdriver.Chrome("G:\python\python-learning\chromedriver_win32\chromedriver.exe",chrome_options=options)
url = 'https://n.cbg.163.com/cbg/query.py?serverid=1&act=search_role'
driver.get(url)
xpath = '/html/body/div[3]/section[2]/table/tbody/tr/td[10]/a'
res = driver.find_elements_by_xpath(xpath)
urlArr = []
for i in res:
    driver.get(i.get_attribute("href"))

    val = driver.find_element_by_css_selector('#roleContent > section > div:nth-child(4) > ul > li:nth-child(7) > span.val')
    # urlArr.append(val)
print(urlArr)

