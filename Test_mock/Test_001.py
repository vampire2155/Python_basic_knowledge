import requests,urllib3,json
urllib3.disable_warnings()

# url = 'https://127.0.0.1:440/demo3'
# headers = {"Content-Type":"application/x-www-form-urlencoded"}
# form_data = {"key":"value"}
# res = requests.post(url,data=form_data,headers=headers,verify=False)
# res.encoding = 'unicode-escape'
# print (res.text)

# url = 'https://127.0.0.1:440/demo4'
# headers = {"Content-Type":"application/x-www-form-urlencoded"}
# data = {"json_key":"json_value","json_key1":"json_value1"}
# json_data = json.dumps(data)  #请求体参数为json时，需要把从json文件中获取到的数据转换成json类型。
# res = requests.post(url,data=json_data,headers=headers,verify=False)
# res.encoding = 'unicode-escape'
# print (res.text)

# url = 'https://127.0.0.1:440/demo5'
# headers = {"Content-Type":"application/x-www-form-urlencoded"}
# form_data = {"key1":"value1","key2":"value"}
# res = requests.post(url,data=form_data,headers=headers,verify=False)
# res.encoding = 'utf-8'
# print (res.text)


# url = 'http://127.0.0.1:1234/trade/purchase'
# headers = {"Content-Type":"application/json"}
# json_data = {
#         "out_trade_no":"20150320010101001",
#         "auth_code":"28763443825664394",
#         "subject":"Iphone6 16G",
#         "buyer_id":"2088202954065786",
#         "seller_id":"2088102146225135",
#         "total_amount":"88.88"
#         }
# res = requests.post(url,json=json_data,headers=headers)
# res.encoding = 'utf-8'
# print (res.text)

#登录接口
# url = 'https://127.0.0.1:440/api/mgr/loginReq'
# headers = {"Content-Type":"application/x-www-form-urlencoded"}
# form_data = {
#             "username":"auto",
#             "password":"sdfsdfsdf"
#             }
# res = requests.post(url,data=form_data,headers=headers,verify=False)
# res.encoding = 'unicode-escape'
# print (res.text)


#增加课程接口
# import json
# url = 'https://127.0.0.1:440/rest/ac01CrmController'
# header = {'X-AUTH-TOKEN':"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmYW5jbCIsInN1YiI6ImZhbmNsIiwiaWF0IjoxNTUwODI2NjI4fQ.610ca0Np-OxDRHew0TyJIScqnBAeeUQs9ir6zRXtp_4",
#           'Content-Type':'application/json'}
# json_data = {
#             "aac003":"张三",
#             "aac004":"1",
#             "aac011":"21",
#             "aac030":"13575726577",
#             "aac01u":"88002255",
#             "crm003":"1",
#             "crm004":"1",
#             "crm00a":"2018-11-11",
#             "crm00b":"aaaaaa",
#             "crm00c":"2019-02-28",
#             "crm00d":"bbbbbb"
#             }
# res = requests.post(url,json=json_data,headers=header,verify=False)
# print (res.text)
# print (res.json())






