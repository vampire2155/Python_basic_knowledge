import requests
from config import HOST
from APITest.classManageAPI.login import login
user_cookie = login()
url = f'{HOST}/api/mgr/sq_mgr/'
form_data = {'action':'add_training',
             'data':
                 '''{
                 "name":"培训班名称-add3",
                 "courselist":"[]",
                 "desc":"描述1-add3",
                 "display_idx":5
                 }'''
             }
res = requests.post(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)