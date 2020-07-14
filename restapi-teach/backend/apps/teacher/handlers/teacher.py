# coding=utf-8


from lib.common import AbstractHandler
from services.datamodel.common.models import Teacher,Lesson,StudentCheckin, Training,TrainingGrade,Student

from apps.teacher.share import app_logger
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from datetime import datetime,timedelta
from django.utils import timezone
import json

class Handler(AbstractHandler):

    def __init__(self):
        AbstractHandler.__init__(self,app_logger)

        self.METHOD_TAB = {
            'GET' : {
                'getmyinfo': self.handle_get_my_info,
                'get_teach_courses': self.handle_get_teach_courses,
                'list_lesson': self.handle_list_lesson,

                'list_training': self.handle_list_training,
                'list_training_grade': self.handle_list_training_grade,

                'list_lesson_checkins': self.handle_list_lesson_checkins,
            },

            'POST': {
                'add_lesson': self.handle_add_lesson,
                'get_classstudent_checkins': self.handle_get_classstudent_checkins, # 某个班级学生签到记录
            },
            

            'PUT' : {
                'changeuserpassword': self.handle_change_userpassword,
                'modify_lesson': self.handle_modify_lesson,
            },


            'DELETE': {
                'delete_lesson': self.handle_delete_lesson,
            },
        }


    def handle_get_teach_courses(self, request):
        teacherid = request.session['teacherid']
        clist, cidlist = Teacher.get_teach_courses(teacherid)

        return JsonResponse({'retcode': 0, 'retlist': clist})


    def handle_list_lesson(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])

        teacherid = request.session['teacherid']
        clist, cidlist = Teacher.get_teach_courses(teacherid)
        paramdict = request.param_dict.dict()
        paramdict['course_ids'] = cidlist

        return JsonResponse(Lesson.list(pagenum,pagesize,paramdict))

    def handle_list_lesson_checkins(self, request):
        self.checkMandatoryParams(request,['lessonid'])
        lessonid = request.param_dict['lessonid']
        return JsonResponse(StudentCheckin.listRecords_by_lesson(lessonid))

    def handle_list_training(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(Training.list(pagenum,pagesize))

    def handle_list_training_grade(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(TrainingGrade.list(pagenum,pagesize))


    def handle_get_my_info(self, request):

        teacherid = request.session['teacherid']
        ret = Teacher.getone(teacherid)

        return JsonResponse(ret)


    # 获取班级学生签到信息
    def handle_get_classstudent_checkins(self, request):
        self.checkMandatoryParams(request,['traininggrade_id','checkinlist'])
        classid = request.param_dict['traininggrade_id']
        # 该课全体学生签到名单
        lessonCheckinlist = json.loads(request.param_dict['checkinlist'])
        sidOfCheckin = [one['student__id'] for one in lessonCheckinlist]
        cStudents = Student.getOneClassStudent(classid)
        for one in cStudents:
            if one['id'] in sidOfCheckin:
                one['ci'] = True
            else:
                one['ci'] = False

        return JsonResponse({'retcode':0,'retlist':cStudents})

    def handle_add_lesson(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Lesson.add(data,request.user.id))

    def handle_change_userpassword(self, request):

        self.app_logger.debug("handle_change_userpassword")

        self.checkMandatoryParams(request,['oldpassword','newpassword'])

        param_dict = request.param_dict


        ret = Teacher.changePasswordByTeacher(request.user.id,
                                                 param_dict['oldpassword'],
                                                 param_dict['newpassword'])


        return JsonResponse(ret)

    def handle_modify_lesson(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return  JsonResponse(Lesson.modify(request.param_dict['id'],newData))



    def handle_delete_lesson(self, request):
        self.checkMandatoryParams(request,['id'])
        Lesson.objects.filter(id=request.param_dict['id']).delete()
        return JsonResponse({'retcode':0})

teacher_handler = Handler()
