import requests
from APITest.classManageAPI.login import login  #从模块login 中调用函数
user_cookie = login()
HOST = 'http://127.0.0.1:9000'
url = f'{HOST}/apijson/mgr/sq_mgr/'
header = {'Content-Type':'application/json'}
json_data = {
              "action":"add_course_json",
              "data":
                  {
                "name":"初中体育2",
                "desc":"初中体育课程2",
                "display_idx":"4"
                  }
            }
res = requests.post(url,json=json_data,cookies=user_cookie,headers=header) #headers不加也是可以的
res.encoding = 'unicode-escape'
print (res.text)