#安装requerts 进行HTTP请求
#pipenv install requests
import requests
class HTTP:
    @staticmethod#classmethod也表示静态 需要多加个变量cls
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json() if return_json else r.text
        else:
            return {} if return_json else ""
