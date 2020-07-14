# 赶集网登录接口实现

import requests
HOST = 'https://passport.ganji.com:443'
url = f'{HOST}/login.php?callback=jQuery182021793244609035112_1592495153999'
form_data = {'username':'vampire2155','password':'441506448',
             'source':'passport',
             '__hash__':'fS3Bpvlk0I6tJ85C//RFyCwa1ye7/FuuoMgTMukJLVVthx8T/ZrE8L8Gj/aRp3s8',
             'setcookie':0,'next':'/','checkCode':''}
res = requests.post(url,data=form_data)
print (res.text)





