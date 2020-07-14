# coding=utf-8


from lib.common import AbstractHandler

from services.datamodel.common.models import Course,Teacher,\
    User,Training,TrainingGrade,Lesson,Student,StudentCheckin
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse

from apps.mgr.share import app_logger
import json





class CommonHandler(AbstractHandler):

    def __init__(self):
        AbstractHandler.__init__(self,app_logger)

        self.METHOD_TAB = {

            'GET': {
                'list_course': self.handle_list_course,
                'list_teacher': self.handle_list_teacher,
                'list_training': self.handle_list_training,
                'list_training_grade': self.handle_list_training_grade,
                'list_lesson': self.handle_list_lesson,
                'list_student': self.handle_list_student,

                'list_lesson_checkins': self.handle_list_lesson_checkins,

                'list_student_checkins': self.handle_list_student_checkins,

            },

            'POST': {
                'add_course': self.handle_add_course,
                'add_course_json': self.handle_add_course_json,
                'add_teacher': self.handle_add_teacher,
                'add_training': self.handle_add_training,
                'add_training_grade': self.handle_add_training_grade,
                'add_lesson': self.handle_add_lesson,
                'add_student': self.handle_add_student,

                'get_classstudent_checkins': self.handle_get_classstudent_checkins,  # 某个班级学生签到记录
            },

            'PUT': {
                'modify_course': self.handle_modify_course,
                'modify_teacher': self.handle_modify_teacher,
                'modify_training': self.handle_modify_training,
                'modify_training_grade': self.handle_modify_training_grade,
                'modify_lesson': self.handle_modify_lesson,
                'modify_student': self.handle_modify_student,

                'changeuserpassword': self.handle_change_userpassword,
            },

            'DELETE': {
                'delete_course': self.handle_delete_course,
                'delete_teacher': self.handle_delete_teacher,
                'delete_training': self.handle_delete_training,
                'delete_training_grade': self.handle_delete_training_grade,
                'delete_lesson': self.handle_delete_lesson,
                'delete_student': self.handle_delete_student,
            },

            #'DELETE' : self.handle_delete
        }




    #  list  *****************

    def handle_list_course(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        try:
            pagenum = int(request.param_dict['pagenum'])
            pagesize = int(request.param_dict['pagesize'])
        except:
            pagenum=0
            pagesize=20
            #return {'retcode': 2, 'reason': '页码或者每页显示数据条数错误'}

        return JsonResponse(Course.list(pagenum,pagesize))


    def handle_list_teacher(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(Teacher.list(pagenum,pagesize))

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

    def handle_list_lesson(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(Lesson.list(pagenum,pagesize,request.param_dict))

    def handle_list_student(self, request):
        self.checkMandatoryParams(request,['pagenum','pagesize'])
        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(Student.list(pagenum,pagesize,request.param_dict))


    def handle_list_lesson_checkins(self, request):
        self.checkMandatoryParams(request,['lessonid'])
        lessonid = request.param_dict['lessonid']
        return JsonResponse(StudentCheckin.listRecords_by_lesson(lessonid))

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


    def handle_list_student_checkins(self, request):

        self.checkMandatoryParams(request,['pagenum','pagesize','studentid'])
        studentid = request.param_dict['studentid']

        pagenum = int(request.param_dict['pagenum'])
        pagesize = int(request.param_dict['pagesize'])
        return JsonResponse(StudentCheckin.listRecords_by_student(pagenum,pagesize,request.param_dict,studentid))


    #  add  *****************

    def handle_add_course(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Course.add(data))


    def handle_add_course_json(self, request):

        self.checkMandatoryParams(request,['data'])
        data = request.param_dict['data']
        return  JsonResponse(Course.add(data))


    def handle_add_teacher(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Teacher.add(data))

    def handle_add_training(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Training.add(data))

    def handle_add_training_grade(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(TrainingGrade.add(data))

    def handle_add_lesson(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Lesson.add(data,request.user.id))

    def handle_add_student(self, request):
        self.checkMandatoryParams(request,['data'])
        data = json.loads(request.param_dict['data'])
        return  JsonResponse(Student.add(data))



    #  modify *****************

    def handle_modify_course(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return  JsonResponse(Course.modify(request.param_dict['id'],newData))


    def handle_modify_teacher(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return JsonResponse(Teacher.modify(request.param_dict['id'],newData))

    def handle_modify_training(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return JsonResponse(Training.modify(request.param_dict['id'],newData))

    def handle_modify_training_grade(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return JsonResponse(TrainingGrade.modify(request.param_dict['id'],newData))

    def handle_modify_lesson(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return  JsonResponse(Lesson.modify(request.param_dict['id'],newData))

    def handle_modify_student(self, request):
        self.checkMandatoryParams(request,['id','newdata'])
        newData = json.loads(request.param_dict['newdata'])
        return  JsonResponse(Student.modify(request.param_dict['id'],newData))




    def handle_change_userpassword(self, request):

        self.app_logger.debug("handle_change_userpassword")

        self.checkMandatoryParams(request,['uid'])

        try:
            user = User.objects.get(id=request.param_dict['uid'])
        except User.DoesNotExist:
            return JsonResponse({'retcode': 1, 'reason': u'没有此用户'})

        # if not check_password(request.param_dict['oldpassword'], user.password):
        #     return JsonResponse({'retcode': 1, 'reason': u'原密码错误'})

        user.password = make_password('sq666')

        try:
            user.save()
        except :
            return JsonResponse({'retcode': 1, 'reason': u'修改用户密码失败'})

        return JsonResponse({'retcode': 0})


    #  delete *****************
    def handle_delete_course(self, request):
        try:
            try:
                id = int(request.param_dict['id'])
                print(id)
                if id<1 :
                    return JsonResponse({'retcode': 2, 'reason': u'传入的id必须大于0'})

            except:
                return JsonResponse({'retcode': 2, 'reason': u'传入的id必须为整数'})

            self.checkMandatoryParams(request,['id'])
            Course.objects.filter(id=request.param_dict['id']).delete()
            return JsonResponse({'retcode':0})
        except:
            return JsonResponse({'retcode': 2,'reason':u'传入参数错误'})


    def handle_delete_teacher(self, request):
        self.checkMandatoryParams(request,['id'])
        return JsonResponse(Teacher.deleteOne(request.param_dict['id']))


    def handle_delete_training(self, request):
        self.checkMandatoryParams(request,['id'])
        Training.objects.filter(id=request.param_dict['id']).delete()
        return JsonResponse({'retcode':0})


    def handle_delete_training_grade(self, request):
        self.checkMandatoryParams(request,['id'])
        TrainingGrade.objects.filter(id=request.param_dict['id']).delete()
        return JsonResponse({'retcode':0})


    def handle_delete_lesson(self, request):
        self.checkMandatoryParams(request,['id'])
        Lesson.objects.filter(id=request.param_dict['id']).delete()
        return JsonResponse({'retcode':0})


    def handle_delete_student(self, request):
        self.checkMandatoryParams(request,['id'])
        return JsonResponse(Student.deleteOne(request.param_dict['id']))



commonHandler = CommonHandler()














