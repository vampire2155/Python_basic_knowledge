import requests,json
from config import HOST
from pprint import pprint
from APITest.classManageAPI.login import login
user_cookie = login()
url = f'{HOST}/api/mgr/sq_mgr/?action=list_training&pagenum=1&pagesize=100'
form_data = {'action':'list_training','pagenum':1,'pagesize':100}
res = requests.get(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
trainClass_id = res.json()['retlist'][0]['id']
# print (trainClass_id)
# print (type(trainClass_id))