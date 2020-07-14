# import pytest
# @pytest.mark.parametrize('x,y',[(1,2,3),(2,3,4)])
# def test001(x,y):
#     print ('------------------')
#     assert x+y == 5
#
# if __name__ == '__main__':
#     pytest.main(['-s'])


# import platform
# import os
# print(f'name--{os.name}')
# print(platform.system())
# print(platform.release())


import requests
#经验证 不加stream和加上stream结果是一样的。需要看一下 stream表示什么含义
# r = requests.get('https://api.github.com/events', stream=True)
# print (r.raw)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload,verify=False)
# print (r.text)




