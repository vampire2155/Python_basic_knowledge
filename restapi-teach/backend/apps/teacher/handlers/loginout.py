# coding=utf-8

import os

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.middleware import csrf

from apps.teacher.share import app_logger
from project.settings_common import USER_TYPE
from services.datamodel.common.models import Teacher

class ReqHandler():
    def __init__(self):

        self.curDir = os.path.dirname(os.path.abspath(__file__))





    def loginReq(self,request):

        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        user = authenticate(username=userName, password=passWord)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                # app_logger.debug("User is valid, active and authenticated")
                if hasattr(user, 'teacher') :
                    is_first_login = False if user.last_login else True
                    login(request, user)
                    request.session['ut'] = USER_TYPE.TEACHER # user type 2 means teacher
                    request.session['teacherid'] = user.teacher.id
                    request.session['realname'] = user.teacher.realname
                    return JsonResponse({'retcode': 0,'realname':user.teacher.realname,'isfirstlogin':is_first_login})
                else:
                    return JsonResponse({'retcode':1,'reason':u'请使用老师账户登录'})
            else:
                return JsonResponse({'retcode':1,'reason':u'用户已经被禁用'})
        else:
            return JsonResponse({'retcode': 1,'reason':u'用户或者密码错误'})




    def logoutReq(self,request):
        logout(request)
        return JsonResponse({'retcode': 0})


handler = ReqHandler()
