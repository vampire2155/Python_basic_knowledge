import requests
HOST = 'http://47.96.181.17:9090'
url = f'{HOST}/rest/toController'
header = {'Content-Type':'application/json'}
json_data = {"userName":"J201903070064","password":"362387359"}
res = requests.post(url,json=json_data)
token = res.json()['token']
print (token)
# print (f'-------------------{res.json()}---------')




