import requests
def login(username='auto',password='sdfsdfsdf'):
    HOST = 'http://127.0.0.1:9000'
    url = f'{HOST}/api/mgr/loginReq'
    headers = {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '311', 'Content-Type': 'application/x-www-form-urlencoded'}
    form_data = {
                'username':username,
                'password':password
                }
    # form_data = 'username=auto&password=sdfsdfsdf'  #data
    res = requests.post(url,data=form_data)
    res.encoding = 'unicode-escape'
    # cookie = res.cookies # 关联方法一：直接把返回的cookie值传递给需要的接口
    # print (cookie)
    return res.cookies
if __name__ == '__main__':
    print (login())



