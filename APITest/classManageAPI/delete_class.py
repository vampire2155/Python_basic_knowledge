import requests
from APITest.classManageAPI.login import login  #从模块login 中调用函数
def deleteClassAPI(data):
    user_cookie = login()
    Host = 'http://127.0.0.1:9000'
    url = f'{Host}/api/mgr/sq_mgr/'
    res = requests.delete(url,data=data,cookies=user_cookie)
    res.encoding = 'unicode-escape'
    return res.json()

if __name__ == "__main__":
    data = {"action":"delete_course","id":"123321"}
    print (deleteClassAPI(data))
    print (type(deleteClassAPI(data)))


