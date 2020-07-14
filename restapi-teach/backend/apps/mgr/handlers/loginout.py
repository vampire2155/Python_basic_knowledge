# coding=utf-8

import os

from django.http import JsonResponse
from django.contrib.auth import authenticate, load_backend,login, logout
from django.shortcuts import redirect
from django.middleware import csrf


from django.conf import settings as django_settings
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

from apps.mgr.share import app_logger,CheckUserIsAdminForApiCaller
from django.core.cache import cache
import datetime

class ReqHandler():
    OK_Admin_Login = JsonResponse({'retcode': 0})

    def __init__(self):

        self.curDir = os.path.dirname(os.path.abspath(__file__))

    def login(self,request):
        csrf.get_token(request)

        #request.session.modified = True
        return redirect('/mgr/login/login.html')
        #return HttpResponse('ok')

    def checkAdminLogin(self,request):

        ret = CheckUserIsAdminForApiCaller(request)
        if ret != True:
            return ret
        else:
            return self.OK_Admin_Login


    def loginReq(self,request):
        #sessionTable = request.session
        #print request.POST


        # if 'passWord' in sessionTable: # already login, just reuse the login logic
        #     userName = sessionTable['userName']
        #     passWord = sessionTable['passWord']
        # else:
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        user = authenticate(username=userName, password=passWord)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                # app_logger.debug("User is valid, active and authenticated")
                if user.is_superuser:
                    login(request, user)
                    request.session['ut'] = 1 # user type 1 means admin
                    return JsonResponse({'retcode': 0})
                else:
                    return JsonResponse({'retcode':1,'reason':u'请使用管理员账户登录'})
            else:
                # app_logger.debug("The password is valid, but the account has been disabled!")
                return JsonResponse({'retcode':0,'reason':'用户已经被禁用'})
        else:
            # the authentication system was unable to verify the username and password
            # app_logger.debug("The username and password were incorrect.")
            return JsonResponse({'retcode': 1,'reason':'用户或者密码错误'})

    def loginMd5(self,request):
        #sessionTable = request.session
        #print request.POST


        # if 'passWord' in sessionTable: # already login, just reuse the login logic
        #     userName = sessionTable['userName']
        #     passWord = sessionTable['passWord']
        # else:
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        user = authenticate(username=userName, password=passWord)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                # app_logger.debug("User is valid, active and authenticated")
                if user.is_superuser:
                    login(request, user)
                    request.session['ut'] = 1 # user type 1 means admin
                    return JsonResponse({'retcode': 0})
                else:
                    return JsonResponse({'retcode':1,'reason':u'请使用管理员账户登录'})
            else:
                # app_logger.debug("The password is valid, but the account has been disabled!")
                return JsonResponse({'retcode':0,'reason':'用户已经被禁用'})
        else:
            # the authentication system was unable to verify the username and password
            # app_logger.debug("The username and password were incorrect.")
            return JsonResponse({'retcode': 1,'reason':'用户或者密码错误'})


    def logoutReq(self,request):
        logout(request)
        return JsonResponse({'retcode': 0})


    # @csrf_exempt
    # def restoreToMgr(self,request):
    #     """
    #     Restore an original login session, checking the signed session
    #     """
    #
    #     original_user_pk = request.session.get('mgr_pk')
    #     logout(request)
    #
    #     if not original_user_pk:
    #         return
    #
    #     u = User.objects.get(pk=original_user_pk)
    #
    #     if not u:
    #         return JsonResponse({'retcode': 1, 'reason': u'用户不存在'})
    #
    #     # Find a suitable backend.
    #     if not hasattr(u, 'backend'):
    #         for backend in django_settings.AUTHENTICATION_BACKENDS:
    #             if u == load_backend(backend).get_user(u.pk):
    #                 u.backend = backend
    #                 break
    #
    #
    #     if hasattr(u, 'backend'):
    #
    #         login(request, u)
    #         request.session['ut'] = 1
    #
    #         return JsonResponse({'retcode': 0})
    #     else:
    #         return JsonResponse({'retcode': 1, 'reason': u'no backend'})


    @csrf_exempt
    def mgrToOtherRole_step2(self,request):
        # if not request.session['ut']:
        #     return JsonResponse({'retcode': 1, 'reason': u'先用管理员帐号登陆'})

        token = request.POST.get('token')
        userinfo = cache.get(token)
        if not userinfo:
            return JsonResponse({'retcode': 1, 'reason': u'管理员快捷登录链接只能使用一次!'})

        cache.delete(token)

        userid   = userinfo['uid']
        usertype = userinfo['utype']

        u = User.objects.get(id=userid)

        # Find a suitable backend.
        if not hasattr(u, 'backend'):
            for backend in django_settings.AUTHENTICATION_BACKENDS:
                if u == load_backend(backend).get_user(u.pk):
                    u.backend = backend
                    break

        # Log the user in.
        # ADMIN   = 1
        # TEACHER = 2
        # STDUENT = 3
        # PARENTS = 4
        # DATAINPUTER = 1001


        if hasattr(u, 'backend'):

            login(request, u)
            if usertype == 2: # Teacher:
                request.session['ut'] = 2
                request.session['realname'] = u.teacher.realname
                request.session['teacherid'] = u.teacher.id
                request.session['schoolid'] = u.teacher.schoolid
            elif usertype  == 3: #  Student:
                request.session['ut'] = 3
                request.session['studentid'] = u.student.id
                request.session['realname'] = u.student.realname
                request.session['schoolid'] = u.student.schoolid
                request.session['gradeid'] = u.student.gradeid
                request.session['classid'] = u.student.classid

            return JsonResponse({'retcode': 0, 'usertype': usertype})
        else:
            return JsonResponse({'retcode': 1, 'reason': u'no backend'})

handler = ReqHandler()
