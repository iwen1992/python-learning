import pymysql
import time
import json
import traceback
import requests
def getDetail():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.get(url,headers=header)
    jsonD=json.loads(res.text)
    data = json.loads(jsonD['data'])
    chinaTotal = data['chinaTotal']
    chinaAdd = data['chinaAdd']
    history = {}
    details = []
    update_time = data['lastUpdateTime']
    history[update_time] = {"confirm": chinaTotal['confirm'], "suspect": chinaTotal['suspect'], "heal": chinaTotal['heal'],"dead": chinaTotal['dead']}
    history[update_time].update({"confirm_add":chinaAdd["confirm"],"suspect_add":chinaAdd['suspect'],"heal_add":chinaAdd['heal'],"dead_add":chinaAdd['dead']})
    data_provice = data['areaTree'][0]['children']
    for pro_info in data_provice:
        provice = pro_info['name']
        for city_info in pro_info['children']:
            city = city_info['name']
            confirm = city_info['total']['confirm']
            confirm_add = city_info['total']['confirm']
            heal = city_info['total']['heal']
            dead = city_info['total']['dead']
            details.append([update_time,provice,city,confirm,confirm_add,heal,dead])
    return details,history
def get_conn():
    conn = pymysql.connect(host="localhost",user="root",password="Wg83saSaGcHHezfK",db="feiyan",charset="utf8")
    cursor = conn.cursor()
    return conn,cursor
def close_conn(conn,cursor):
    if conn:
        conn.close()
    if cursor:
        cursor.close()
def updata_details():
    cursor = None
    conn = None
    try:
        li = getDetail()[0]
        conn,cursor=get_conn()
        sql = "insert into detail(update_time,provice,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from detail order by id desc limit 1)"
        cursor.execute(sql_query,li[0][0])
        if not cursor.fetchone()[0]:
            print("开始更新数据")
            for item in li:
                cursor.execute(sql,item)
            conn.commit()
            print("更新数据完毕")
        else:
            print("已是最新数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)
def updata_history():
    cursor = None
    conn = None
    conn,cursor = get_conn()
updata_details()

