import requests
HOST = 'http://127.0.0.1:81'
url = f'{HOST}/zentao/doc-create-product-0-0-0-doc.html'
header = {'Content-Type':'application/x-www-form-urlencoded'}
file = open(r'C:\Users\Vampire\Desktop\软件测试工具安装包\软件测试最新简历模板.docx','rb')
form_data = {
            'Content-Disposition: form-data; name="product"':'1',
            'Content-Disposition: form-data; name="module"':'0',
            'Content-Disposition: form-data; name="type"':'file',
            'Content-Disposition: form-data; name="title"':'create0615',
            'Content-Disposition: form-data; name="url"':'',
            'Content-Disposition: form-data; name="content"':'',
            'Content-Disposition: form-data; name="keywords"':'create0615',
            'Content-Disposition: form-data; name="digest"':'create0615',
            '''Content-Disposition: form-data; name="files[]"; filename="软件测试最新简历模板.docx"
Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document''':file,
            'Content-Disposition: form-data; name="labels[]"':'',
            'Content-Disposition: form-data; name="lib"':'product'
            }
res = requests.post(url,data=form_data)
print (res.text)






