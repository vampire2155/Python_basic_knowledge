import requests
from APITest.classManageAPI.login import login
user_cookie = login()
HOST = 'http://127.0.0.1:9000'
url = f'{HOST}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {'action':'add_teacher',
             'data':
                 '''{
                    "username":"liwu6",
                    "password":"sq888",
                    "realname":"liwu123456",
                    "desc":"物理老师",
                    "courses":[],
                    "display_idx":1
                    }
                 '''
            }
res = requests.post(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)


