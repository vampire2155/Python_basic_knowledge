import requests
import hashlib  #导入算法库
from random import randint
telnum = randint(10,99)  #电话号码给定了前9位，后2位是随机的
pwd = hashlib.md5(b'zr111111hg').hexdigest()  #获取16进制的值
HOST = 'http://121.41.14.39:2001'
url = f'{HOST}/token/token'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {'mobile':f'135880000{telnum}','password':pwd}
res = requests.post(url,data=form_data,headers=header)
print (res.json())






