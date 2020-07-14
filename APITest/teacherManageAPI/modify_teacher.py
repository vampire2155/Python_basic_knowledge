import requests
from pprint import pprint
from APITest.teacherManageAPI.list_teacher import teacher_id
from APITest.classManageAPI.login import login
user_cookie = login()
HOST = 'http://127.0.0.1:9000'
url = f'{HOST}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {'action':'modify_teacher',
             'id':f'{teacher_id}',
             'newdata':
             '''{
                "username":"lishiming",
                "password":"sq8888",
                "realname":"李民",
                "desc":"老师",
                "courses":[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}],
                "display_idx":2
                }
                '''
             }
res = requests.put(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)