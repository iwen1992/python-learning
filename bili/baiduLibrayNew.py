from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--user-agent="Baiduspider"')
options.add_argument('--headless')
brower = webdriver.Chrome('G:\python\python-learning\chromedriver_win32\chromedriver.exe',chrome_options=options)
docUrl = 'https://wenku.baidu.com/view/b33c8c772c3f5727a5e9856a561252d380eb2014.html?fr=search-1-aladdin-incomeN-score_2'
def get_htmlSouce():
    url = input("请输入你要下载的文档链接")
    brower.get(url)
    title = brower.find_elements_by_xpath('//*[@id="doc-tittle-0"]')
    content = brower.find_elements_by_xpath('//*[@id="doc-main"]/div/div[2]/div')
    tit = ''
    con = ''
    for titleI in title:
        tit = str(titleI.text)
        tit = tit.replace('/','')
    for contentI in content:
        con = contentI.text
    try:
        with open(r'baidu/%s.txt' % tit, 'w', encoding='utf-8') as f:
            f.write(con)
    except:
        print('error')
    finally:
        print('<%s>下载完毕！' % tit)
    # more_doc = 'docment.getElementsByClassName("read-all")[0].click()'
    # brower.execute_script(more_doc)
    # brower.implicitly_wait(15)
get_htmlSouce()

