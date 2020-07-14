import requests
HOST = 'https://i.cnblogs.com'
url = f'{HOST}/api/images/1789962'
json_data = {"fileName":"汇丰线要求.jpg","sizeInBytes":136136,"visible":'false',"title":"请求"}
res = requests.post(url,json=json_data)
res.encoding = 'unicode-escape'
print (res.text)






