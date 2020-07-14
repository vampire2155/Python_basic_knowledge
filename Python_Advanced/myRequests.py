# -*- coding: utf-8 -*-
import requests
from Python_Advanced.myLog import apiLog
from Python_Advanced.myLog import decoratelog

class MyRequests:
    def __init__(self, url):
        # 记住一些持久性信息 cookie、连接池、配置
        self.session = requests.session()
        # 请求的网址
        self.url = url
        # 超时时间
        self.timeout = 10
        # 错误消息
        self.errorMsg = ""

    @decoratelog
    def post(self, bodyData=None, bodyJson=None, **kwargs):
        """
        原始 post 的二次封装
        :param bodyData:
        :param bodyJson:
        :param kwargs:
        :return:
        """
        response = None
        try:
            response = self.session.post(self.url, data=bodyData, json=bodyJson, timeout=self.timeout, **kwargs)
            apiLog.info("请求参数：%s" % bodyData if bodyData else bodyJson)
            apiLog.info("请求结果：%s" % response.text)
        except Exception as e:
            self.errorMsg = str(e)
            raise Exception("HTTP 请求异常，异常信息\n%s" %self.errorMsg)
        return response


if __name__ == '__main__':
    r = MyRequests("https://api.com//station2s")
    payload = {
        "appkey": "your_appkey_here",
        "start": "北京",
        "end": "杭州",
        "ishigh": 0
    }
    r.post(bodyData=payload)
