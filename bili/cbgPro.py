from selenium import webdriver
import re
import pymysql
import time
import traceback
options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
# options.add_argument('--proxy-server=http://ip:port')
#options.add_argument("--headless")
driver = webdriver.Chrome("G:\python\python-learning\chromedriver_win32\chromedriver.exe",chrome_options=options)
counter = int(1)
resArr = []
cbgArr = []
telArr = []
times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def get_conn():
    conn = pymysql.connect(host="localhost",user="root",password="Wg83saSaGcHHezfK",db="cbg",charset="utf8")
    cursor = conn.cursor()
    return conn,cursor
def close_conn(conn,cursor):
    if conn:
        conn.close()
    if cursor:
        cursor.close()
def getItemVal(values):
    cursor = None
    conn = None
    for i in values:
        cbgItem={'url':'','genyue':'','price':'','score':'','hongchen':''}
        url = i
        driver.implicitly_wait(5)
        driver.get(url)
        genyue = driver.find_elements_by_xpath('/html/body/section[1]/section[1]/div[2]/div[1]/div/div/div[2]/section/div[4]/ul/li[7]/span[2]')
        price = driver.find_elements_by_xpath('/html/body/section[1]/section[1]/div[2]/dl/div[6]/dd/span/span')
        score = driver.find_elements_by_xpath('/html/body/section[1]/section[1]/div[2]/div[1]/div/div/div[2]/section/div[1]/div/ul/li[4]/span[2]')
        hongchen = driver.find_elements_by_xpath('/html/body/section[1]/section[1]/div[2]/div[1]/div/div/div[2]/section/div[4]/ul/li[8]/span[2]')
        for genyueI in genyue:
            cbgItem['genyue']= int(genyueI.text)
        for priceI in price:
            cbgItem['price'] = int(float(re.compile(r'(?<=￥)\d+\.?\d*').findall(priceI.text)[0]))
        for scoreI in score:
            cbgItem['score'] = int(scoreI.text)
        for hongchenI in hongchen:
            cbgItem['hongchen'] = int(hongchenI.text)
        cbgItem['url']=url
        if(cbgItem['price'] and cbgItem['genyue']):

            if(cbgItem['price']<2000 and cbgItem['genyue']>10000):
                telArr.append(cbgItem)
                try:
                    conn, cursor = get_conn()
                    sql = "insert into cbg_good(genyue,price,score,hongcheng,url,thetime) values(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, [cbgItem['genyue'],cbgItem['price'],cbgItem['score'],cbgItem['hongchen'],cbgItem['url'],times])
                    conn.commit()
                except:
                    traceback.print_exc()
                finally:
                    close_conn(conn, cursor)

        try:
            conn, cursor = get_conn()
            sql = "insert into cbg_all(genyue,price,score,hongcheng,url,thetime) values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, [cbgItem['genyue'], cbgItem['price'], cbgItem['score'], cbgItem['hongchen'],cbgItem['url'],times])
            conn.commit()
        except:
            traceback.print_exc()
        finally:
            close_conn(conn, cursor)
        cbgArr.append(cbgItem)
while counter <= 528:
    urlArr = []
    url = 'https://n.cbg.163.com/cbg/query.py?page='+str(counter)+'&act=search_role'
    driver.implicitly_wait(5)
    driver.get(url)
    xpath = '/html/body/div[3]/section[2]/table/tbody/tr/td[10]/a'
    pageResult = driver.find_elements_by_xpath(xpath)
    for resI in pageResult:
        uri = resI.get_attribute('href')
        urlArr.append(uri)
    getItemVal(urlArr)
    # for resultI in pageResult:
    #     resArr.append(resultI)
    counter += 1
# url = 'https://n.cbg.163.com/cbg/query.py?serverid=1&act=search_role'
# driver.get(url)
# xpath = '/html/body/div[3]/section[2]/table/tbody/tr/td[10]/a'
# res = driver.find_elements_by_xpath(xpath)
print(cbgArr)
print(telArr)
# result = getItemVal(urlArr)
# print(result)

