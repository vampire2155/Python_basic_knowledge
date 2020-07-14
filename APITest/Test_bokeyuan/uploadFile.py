import requests
HOST = 'https://i.cnblogs.com'
url = f'{HOST}/api/files/?file=222.rar&size=25945'
header = {'Content-Type':'application/json,text/plain,*/*'}
# header = {'Content-Type':'multipart/form-data','Cookie':f'token={token}'}
fileDir = r'C:\Users\Vampire\Desktop\222.rar'
file_data = {'file':('222.rar',open(fileDir,'rb'),"zar")}
res = requests.post(url,files=file_data)
print (res)




