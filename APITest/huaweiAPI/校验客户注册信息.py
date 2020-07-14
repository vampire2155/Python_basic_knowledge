import requests
url = 'http://127.0.0.1:1234/v2/partners/sub-customers/users/check-identity'
headers = {"Content-Type":"application/json","X-Auth-Token":"eyJhbGciOiJIUzI1NiJ9.eyJqdGk"}
json_data ={
            "search_type":"name",
			"search_value":"adADk123"
            }
res = requests.post(url,json=json_data,headers=headers)
res.encoding = 'utf-8'
print (res.json())




