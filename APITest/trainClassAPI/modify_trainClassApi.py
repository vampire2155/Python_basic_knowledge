from APITest.trainClassAPI.list_trainClassApi import trainClass_id
import requests
from APITest.classManageAPI.login import login
from config import HOST
user_cookie = login()
url = f'{HOST}/api/mgr/sq_mgr/'
form_data = {'action':'modify_training',
             'id':trainClass_id,
             'newdata':
             '''
             {"name":"培训班名称_modified",
             "courselist":"[]",
             "desc":"描述12312313_modified",
             "display_idx":1}
             '''
            }
res = requests.put(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)