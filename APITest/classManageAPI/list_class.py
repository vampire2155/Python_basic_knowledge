import requests
from pprint import pprint
from APITest.classManageAPI.login import login
from dataConfig import HOST  #导入配置文件中的HOST参数
def listClassAPI(data):
    user_cookie = login()
    url = f'{HOST}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
    headers = {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '311', 'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.get(url,params=data,cookies=user_cookie)  #不需要headers ，需要搞清楚为什么？ 什么情况下需要填写headers，什么情况下不需要填写headers
    res.encoding = 'unicode-escape'
    # pprint (res.json())
    return res.json()

if __name__ == '__main__':
    data = {'username': '', 'password': ''}
    print (type(data))
    pprint (listClassAPI(data))