import requests
import hashlib
HOST = 'http://127.0.0.1:81'
url = f'{HOST}/zentaoAPI/user-login.html'
header = {'Content-Type':'application/x-www-form-urlencoded'}
psd = hashlib.md5(b'123456').hexdigest()   #经过验证，密码是MD5 加密的。
form_data = {'account':'admin','password':psd,'referer':'http://127.0.0.1:81/zentao/my/'}
res = requests.post(url,data=form_data,headers=header)
print (res.text)  #经验证，结果正确。


