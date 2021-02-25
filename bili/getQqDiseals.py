import json
import requests
def getDetail():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.get(url,headers=header)
    jsonD=json.loads(res.text)
    data = json.loads(jsonD['data'])
    history = []
    history.append(data['chinaTotal'])

    print(history)
    details = []
    update_time = data['lastUpdateTime']
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

getDetail()
