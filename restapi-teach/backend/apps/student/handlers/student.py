# coding=utf-8


from lib.common import AbstractHandler
from services.datamodel.common.models import Student,StudentCheckin,Lesson

from apps.student.share import app_logger
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from datetime import datetime,timedelta
from django.utils import timezone

from random import  randint

class Handler(AbstractHandler):

    def __init__(self):
        AbstractHandler.__init__(self,app_logger)

        self.METHOD_TAB = {
            'GET' : {
                'getmyinfo': self.handle_get_my_info,
                'getmyslessons': self.handle_get_my_slessons,
                'getmyclessons': self.handle_get_my_clessons,
                'listmycheckinrecords': self.handle_list_my_checkinrecords,


                'get_my_notifications': self.get_my_notifications,
                'get_my_tasks': self.get_my_tasks,
                'get_task_questions': self.get_task_questions,
            },

            'POST': {
                'checkin_lesson': self.handle_checkin_lesson,

                'login': self.pf_login,
                'submit_tasks': self.submit_tasks,
            },
            

            'PUT' : {
                'changeuserpassword': self.handle_change_userpassword,
            },

            #'DELETE' : self.handle_delete
        }

    def pf_login(self,request):
        # print('get pf_login')
        return JsonResponse({'retcode':0})

    def get_my_notifications(self,request):
        # print('get_my_notifications')
        return JsonResponse({'retcode':0,
                             'notifications': [
                                 {'type':1,
                                  'nid' :randint(1,10000)},
                                 {'type':2,
                                  'pid' :randint(1,10000)},
                             ]})

    def get_my_tasks(self, request):
        # print('get_my_tasks')
        return JsonResponse({'retcode':0,
                             'tasks': [
                                 {'taskid' :randint(1,10000)},
                                 {'taskid' :randint(1,10000)}
                             ]})

    def get_task_questions(self, request):
        # print('get_task_questions')
        return JsonResponse({'retcode':0,
                             'quesions': [
                                 {'qid' :randint(1,10000)},
                                 {'qid' :randint(1,10000)},
                                 {'qid' :randint(1,10000)},
                                 {'qid' :randint(1,10000)},
                                 {'qid' :randint(1,10000)},
                             ]})

    def submit_tasks(self, request):
        # print('submit_tasks')
        return JsonResponse({'retcode':0})

    def handle_list_my_checkinrecords(self, request):


        self.checkMandatoryParams(request,['pagenum','pagesize'])
        studentid = request.session['studentid']

        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(StudentCheckin.listRecords_by_student(pagenum,pagesize,request.param_dict,studentid))


    def handle_checkin_lesson(self, request):


        self.checkMandatoryParams(request,['lessonid'])
        lessonid = request.param_dict['lessonid']
        studentid = request.session['studentid']
        try:
            lesson = Lesson.objects.get(id=lessonid)
        except:
            return JsonResponse({'retcode':2,'reason':'illegal lessonid'})

        starttime = lesson.starttime

        begin = starttime  - timedelta(minutes=10)
        end   = starttime  + timedelta(minutes=30)

        curTime = timezone.now()
        if curTime < begin:
            return JsonResponse({'retcode':2,'reason':u'签到时间还没有到'})

        if curTime > end:
            return JsonResponse({'retcode':2,'reason':u'签到时间已过'})


        ret = StudentCheckin.addOne(studentid,lessonid)

        return JsonResponse(ret)

    def handle_get_my_info(self, request):

        studentid = request.session['studentid']
        ret = Student.getone(studentid)

        return JsonResponse(ret)


    # get scheduled lessons
    def handle_get_my_slessons(self, request):

        studentid = request.session['studentid']
        ret = Student.getstudentscheduledlessons(studentid)

        return JsonResponse(ret)

    # get checkin lessons
    def handle_get_my_clessons(self, request):

        studentid = request.session['studentid']
        ret = Student.getstudentcheckinlessons(studentid)

        return JsonResponse(ret)

    def handle_change_userpassword(self, request):

        self.app_logger.debug("handle_change_userpassword")

        self.checkMandatoryParams(request,['oldpassword','newpassword'])

        param_dict = request.param_dict


        ret = Student.changePasswordByStudent(request.user.id,
                                                 param_dict['oldpassword'],
                                                 param_dict['newpassword'])


        return JsonResponse(ret)





student_handler = Handler()
