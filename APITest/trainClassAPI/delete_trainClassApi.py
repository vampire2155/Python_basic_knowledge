from APITest.trainClassAPI.list_trainClassApi import trainClass_id
import requests
from APITest.classManageAPI.login import login
from config import HOST
user_cookie = login()
url = f'{HOST}/api/mgr/sq_mgr/'
form_data = {'action':'delete_training','id':trainClass_id}
res = requests.delete(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)









