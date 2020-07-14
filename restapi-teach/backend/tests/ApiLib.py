import requests
from cfg import g_course_url, g_login_url
from pprint import pprint


class AdminOperationSession:

    def __init__(self):
        pass

    def adminlogin(self, username, password):
        payload = {
            'username': username,
            'password': password
        }
        # data参数 就是构造消息体的
        response = requests.post(g_login_url,
                                 data=payload)

        # 获取结果，返回给调用者
        retDict = response.json()
        # 打印出结果
        print(retDict)

        cookies = response.cookies
        self.sessionid = cookies['sessionid']

        return retDict

    def add_course(self, name, desc, displayidx):
        payload = {
            'action': 'add_course',
            # 格式化字符串的方式来构造消息
            'data': '''
            {
            "name":"%s",
            "desc":"%s",
            "display_idx":"%s"
            }''' % (name, desc, displayidx)

        }
        # data参数 就是构造消息体的
        response = requests.post(g_course_url,
                                 data=payload,
                                 cookies={'sessionid': self.sessionid})

        # 获取结果，返回给调用者
        retDict = response.json()
        # 打印出结果
        print(retDict)

        return retDict

    def list_course(self):

        params = {
            'action': 'list_course',
            'pagenum': '1', 'pagesize': 20
        }
        response = requests.get(g_course_url,
                                params=params,
                                cookies={'sessionid': self.sessionid})
        # 获取结果，返回给调用者
        retDict = response.json()
        pprint(retDict)

        # 获取结果，返回给调用者
        return retDict

    def delete_course(self, courseid):
        payload = {
            'action': 'delete_course',
            'id': f'{courseid}'
        }

        response = requests.delete(g_course_url,
                                   data=payload,
                                   cookies={'sessionid': self.sessionid})

        r = response.json()
        pprint(r)
        return r

    def delete_all_course(self):

        # 先列出所有课程
        rd = self.list_course()
        pprint(rd)

        # 没有课程，直接返回
        if rd['total'] == 0:
            return

        # 删除列出的所有课程
        for one in rd['retlist']:
            self.delete_course(one['id'])

        # 再列出所有课程
        rd = self.list_course()
        pprint(rd)

        # 如果没有删除干净，通过异常报错给RF
        if rd['retlist'] != []:
            raise Exception("没有删除干净!!")

    def get_new_course(self, list1, list2):
        return [one for one in list1 if one not in list2]