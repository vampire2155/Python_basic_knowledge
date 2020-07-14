import requests
from pprint import pprint
from APITest.classManageAPI.login import login
user_cookie = login()
HOST = 'http://127.0.0.1:9000'
url = f'{HOST}/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {'action':'list_teacher','pagenum':1,'pagesize':20}
res = requests.get(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
# print (res.json())
teacher_id = res.json()['retlist'][0]['id']
# print (res.json())






