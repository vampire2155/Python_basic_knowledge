import requests
from pprint import pprint
from APITest.strengthening_practice.acquire_token import token
user_cookie = {'token':token}  #需要把cookie 变为字典格式。
HOST = 'http://121.41.14.39:2001'
url = f'{HOST}/user/doUpload'
header = {'Content-Type':'multipart/form-data','Cookie':f'token={token}'}
fileDir = r'C:\Users\Vampire\Downloads\images_logo.png'
file_data = {'file':('images_logo.png',open(fileDir,'rb'),"jpg/png/gif")}
res = requests.post(url,files=file_data,cookies=user_cookie)
pprint (res.json())










