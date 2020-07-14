import requests
from APITest.strengthening_practice.acquire_token import token
from random import randint
from pprint import pprint
tel = randint(10000000,99999999)
HOST = 'http://47.96.181.17:9090'
url = f'{HOST}/rest/ac01CrmController'
header = {'X-AUTH-TOKEN':token,'Content-Type':'application/json'}
json_data = {
            "aac003": "张三",
            "aac004": "1",
            "aac011": "21",
            "aac030": f"135{tel}",
            "aac01u": "88002255",
            "crm003": "1",
            "crm004": "1",
            "crm00a": "2018-11-11",
            "crm00b": "aaaaaa",
            "crm00c": "2019-02-28",
            "crm00d": "bbbbbb"
            }
res = requests.post(url,json=json_data,headers=header)
pprint (res.json())






