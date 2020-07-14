import requests,json
from config import HOST   #导入配置文件中的HOST参数
from APITest.classManageAPI.login import login  #从模块login 中调用函数
user_cookie = login()
def addClassAPI(data):
    #增加课程接口
    url = f'{HOST}/api/mgr/sq_mgr/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    form_data = {
                'action':'add_course',
                'data':data
                }
    res = requests.post(url,data=form_data,cookies=user_cookie)
    res.encoding = 'unicode-escape'
    return res.text

if __name__ == '__main__':
    course_data = '''{
                      "name":"大学英语大学英语大学英语大学英语大学英语",
                      "desc":"大学英语课程",
                      "display_idx":"4"
                      }'''

    print (addClassAPI(course_data))
    print (type(addClassAPI(course_data)))
    print (json.loads(addClassAPI(course_data))["retcode"])
    print(type(json.loads(addClassAPI(course_data))["retcode"]))  #string类型











