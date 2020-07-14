import requests
from pprint import pprint
from APITest.teacherManageAPI.list_teacher import teacher_id
from APITest.classManageAPI.login import login
user_cookie = login()
HOST = 'http://127.0.0.1:9000'
url = f'{HOST}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {'action':'delete_teacher','id':f'{teacher_id}'}
res = requests.delete(url,data=form_data,cookies=user_cookie)
print (res.json())












