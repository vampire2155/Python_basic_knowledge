import requests
from APITest.classManageAPI.login import login  #从模块login 中调用函数
user_cookie = login()
Host = 'http://127.0.0.1:9000'
url = f'{Host}/api/mgr/sq_mgr/'
#  需要把查询课程接口中的返回结果  进行参数化，传递给  下面 的 id参数。
form_data = {
            'action':'modify_course',
            'id':2161,
            'newdata':"""{
                      "name":"初中化学_修改后",
                      "desc":"初中化学课程_修改后",
                      "display_idx":"888"
                    }
                    """
            }
res = requests.put(url,data=form_data,cookies=user_cookie)
res.encoding = 'unicode-escape'
print (res.text)