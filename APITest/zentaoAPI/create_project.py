import requests
HOST = 'http://127.0.0.1:81'
url = f'{HOST}/zentao/project-create.html'
header = {'Content-Type':'application/x-www-form-urlencoded'}
form_data = {
            'name':'vampire',
            'code':'vampire',
            'begin':'2020-06-15',
            'end':'2020-07-31',
            'days':'35',
            'team':'vampire',
            'type':'sprint',
            'products[0]':'1',
            'products[1]':'0',
            'desc':'vampire0615',
            'acl':'open'
}
res = requests.post(url,data=form_data,headers=header)
print (res.text)


