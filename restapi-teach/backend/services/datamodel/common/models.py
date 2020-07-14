# coding=utf-8
from django.db import models
import logging,traceback,re
from django.conf import settings
from lib.common import now
from django.db.models import F
from django.utils.dateparse import parse_datetime

from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import AbstractUser

from django.db import IntegrityError, transaction
from django.contrib.auth.hashers import make_password,check_password
import json
from datetime import datetime,timedelta


model_logger =  logging.getLogger("datamodel")



# class USER_TYPE:
#     ADMIN   = 1
#     TEACHER = 2
#     STDUENT = 3
#
class User(AbstractUser):
    usertype = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=500, null=True, blank=True)
    idcardnumber = models.CharField(max_length=50,null=True, blank=True, db_index=True) #身份证号
    avatar_url = models.URLField(max_length=300, null=True, blank=True)

    phonenumber = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    realname = models.CharField(max_length=30, db_index=True,null=True, blank=True)

    REQUIRED_FIELDS = ['usertype','email']



class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='admin',on_delete=models.PROTECT)

    class Meta:
        db_table = "sq_admin"


def comm_list(model,pagenum,pagesize):
    qs = model.objects.all()

    qs = qs.order_by('display_idx').values()

    pgnt = Paginator(qs, pagesize)

    # retObj = {'total':pgnt, 'content':pgnt.page(pagenum)}
    try:
        retObj = list(pgnt.page(pagenum))
    except EmptyPage:
        #return [], 0
        return {'retcode': 2, 'reason': '页码或者每页显示数据条数错误'}
    return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}

# 课程
class Course(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.CharField(max_length=1500, null=True, blank=True)
    display_idx = models.PositiveSmallIntegerField(default=0) # 展示优先级

    class Meta:
        db_table = "sq_course"


    @staticmethod
    def list(pagenum,pagesize):
        if not (str(pagenum).isdigit()):
            return {'retcode': 2, 'reason':u'页码必须为数字'}
        if not (str(pagesize).isdigit()):
            return {'retcode': 2, 'reason':u'每页显示条数必须为数字'}

        if pagesize<1:
            return {'retcode': 2, 'reason': u'每页显示条数必须大于0'}

        if pagesize>1000:
            return {'retcode': 2, 'reason': u'每页显示条数不能大于1000'}

        return comm_list(Course,pagenum,pagesize)


    @staticmethod
    def add(data):
        try:
            if data['name']=='':
                return {'retcode': 2,
                        "reason": u"课程名为空！"}

            regex = r'^[^\\/:\*\?\@\!\#\$\%\;\.\,\"\'\`\ \！\=\[\]\}\{\:\“\：\。\&\^"<>\|]+$'  # 不能为空，不能含有\/:*?"<>|等字符
            ret= re.match(regex, data['name'])
            print('====')
            print(ret)
            print('====')
            if ret==None:
                return {'retcode': 2,
                        "reason": u"课程名包含特殊字符！"}


            if len(data['name']) > 20:
                return {'retcode': 2,
                        "reason": u"课程名长度大于20！"}

            if not (str(data['display_idx']).isdigit()):
                return {'retcode': 2,
                        "reason": u"展示次序必须为整形数字！"}

            if data['display_idx']=='':
                return {'retcode': 2,
                        "reason": u"展示次序为空！"}




            if int(data['display_idx'])>999:
                return {'retcode': 2,
                        "reason": u"展示次序必须小于1000！"}

            if int(data['display_idx'])<0:
                return {'retcode': 2,
                        "reason": u"展示次序必须大于0！"}

            course = Course.objects.create(name=data['name'],
                              desc=data['desc'],
                              display_idx=data['display_idx'])

            return {'retcode': 0,'id':course.id}

        except IntegrityError:
            return {'retcode': 2,
                    "reason": u"同名课程存在"}




    @staticmethod
    def modify(rid,data):
        if data['name'] == '':
            return {'retcode': 2,
                    "reason": u"课程名为空！"}

        regex = r'^[^\\/:\*\?\@\!\#\$\%\;\.\,\"\'\`\ \！\=\[\]\}\{\:\“\：\。\&\^"<>\|]+$'  # 不能为空，不能含有\/:*?"<>|等字符
        ret = re.match(regex, data['name'])
        print('====')
        print(ret)
        print('====')
        if ret == None:
            return {'retcode': 2,
                    "reason": u"课程名包含特殊字符！"}

        if len(data['name']) > 20:
            return {'retcode': 2,
                    "reason": u"课程名长度大于20！"}

        if not (str(data['display_idx']).isdigit()):
            return {'retcode': 2,
                    "reason": u"展示次序必须为整形数字！"}

        if data['display_idx'] == '':
            return {'retcode': 2,
                    "reason": u"展示次序为空！"}

        if int(data['display_idx']) > 999:
            return {'retcode': 2,
                    "reason": u"展示次序必须小于1000！"}

        if int(data['display_idx']) < 0:
            return {'retcode': 2,
                    "reason": u"展示次序必须大于0！"}

        Course.objects.filter(id=rid)\
                      .update(name=data['name'],
                              desc=data['desc'],
                              display_idx=data['display_idx'])
        return {'retcode': 0}


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher',on_delete=models.PROTECT)
    # 教哪些课
    courses = models.ManyToManyField(Course, related_name='course_teacher')

    realname = models.CharField(max_length=30, db_index=True)

    desc = models.CharField(max_length=1500, null=True, blank=True)
    display_idx = models.PositiveSmallIntegerField(default=0) # 展示优先级

    class Meta:
        db_table = "sq_teacher"

    @staticmethod
    def getone(teacherid):
        try:
            teacher = Teacher.objects.get(id=teacherid)
        except Teacher.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的老师不存在'.format(teacherid)
            }

        info = {
            'realname':teacher.realname,
        }

        return {
            'retcode': 0,
            'info': info
        }

    @staticmethod
    def get_teach_courses(teacherid):
        qs = Course.objects.filter(course_teacher__id=teacherid).values('id','name').order_by('display_idx')
        clist = []
        cidlist = []
        for one in qs :
            # cid = one['id']
            # cname = one['name']
            clist.append(one)
            cidlist.append(one['id'])
        return clist,cidlist

    @staticmethod
    def list(pagenum,pagesize):

        qs = Teacher.objects.select_related('user').all()

        qs = qs.order_by('display_idx').annotate(username=F('user__username'))\
            .values('id','realname','desc','display_idx','username')



        pgnt = Paginator(qs, pagesize)

        # retObj = {'total':pgnt, 'content':pgnt.page(pagenum)}
        try:
            retObj = list(pgnt.page(pagenum))
            for one in retObj:
                qs2 = Teacher.courses.through.objects.filter(teacher_id=one['id']) \
                        .values('course_id')
                one['courses'] = list(qs2)
        except EmptyPage:
            return [], 0

        return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}



    @staticmethod
    def add(data):

        username    = data['username']
        realname    = data['realname']
        try:
            if User.objects.filter(username=username).exists():
                return {'retcode': 1, 'reason': u'登录名 %s 已经存在'%username}

            with transaction.atomic():
                new_user = User.objects.create(
                    username  = username,
                    usertype  = settings.USER_TYPE.TEACHER,
                    password  = make_password(data['password']),
                    last_name = realname,
                    phonenumber  = '',
                    idcardnumber = '',
                    email        = '',
                )

                teacher = Teacher(user=new_user,
                                  realname=realname,
                                  desc=data['desc'],
                                  display_idx=data['display_idx'])

                teacher.save()


                courseidList = [one['id'] for one in  data['courses']]
                teacher.courses.add(*courseidList)

                return {'retcode': 0, 'id': teacher.id}

        except IntegrityError:
            err = traceback.format_exc()
            model_logger.error(err)
        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            return {'retcode': 1, 'reason': err}


    @staticmethod
    def modify(teacherid,data):

        try:
            teacher = Teacher.objects.get(id=teacherid)
        except Teacher.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的老师不存在'.format(teacherid)
            }

        for param in ['realname',  'desc', 'display_idx']:
            if param in data:
                setattr(teacher, param, data[param])

        try:
            with transaction.atomic():
                teacher.save()

                # 可能要更新user表里面的名字
                tu_changed = False
                if 'realname' in data:
                    teacher.user.last_name = data['realname']
                    tu_changed = True
                if 'username' in data:
                    teacher.user.username = data['username']
                    tu_changed = True
                if tu_changed:
                    teacher.user.save()

                # 可能要更新 teacher_course表
                Teacher.courses.through.objects.filter(teacher_id=teacherid).delete()
                for one in data['courses']:
                    teacher.courses.add(one['id'])


                # 这是 节省性能的做法
                # cidListBefore = Teacher.courses.through.objects.filter(teacher_id=teacherid) \
                #             .values_list('course_id', flat=True)
                # cidListAfter = [one['id'] for one in data['courses']]
                # for cid in cidListAfter:
                #     if cid not in cidListBefore:
                #         teacher.courses.add(cid)
                #
                # for cid in cidListBefore:
                #     if cid not in cidListAfter:
                #         teacher.courses.remove(cid)




        except IntegrityError as e:
            return {'retcode': 1, 'reason': str(e)}
        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            raise

        return {'retcode': 0}



    @staticmethod
    def deleteOne(teacherid):

        try:
            teacher = Teacher.objects.get(id=teacherid)
        except Teacher.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的老师不存在'.format(teacherid)
            }

        try:
            with transaction.atomic():
                teacher.delete()

                # 同时要删除user表里对应的
                teacher.user.delete()

        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            raise

        return {'retcode': 0}


    @staticmethod
    def changePasswordByTeacher(userid,oldpassword,newpassword):
        try:
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return {'retcode': 1, 'reason': u'没有此用户'}

        if not check_password(oldpassword, user.password):
            return {'retcode': 1, 'reason': u'原密码错误'}

        user.password = make_password(newpassword)

        try:
            user.save()
        except :
            return {'retcode': 1, 'reason': u'修改用户密码失败'}

        return {'retcode': 0}

# 课程时刻表
class Lesson(models.Model):
    course = models.ForeignKey(Course, blank=False,on_delete=models.PROTECT)
    # name = models.CharField(max_length=200, null=True, blank=True)
    # 有哪些课
    starttime = models.DateTimeField()
    endtime   = models.DateTimeField()

    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_lessons',on_delete=models.PROTECT)

    desc = models.CharField(max_length=1500, null=True, blank=True)

    class Meta:
        db_table = "sq_lesson"

    @staticmethod
    def list(pagenum,pagesize,params):

        qs = Lesson.objects.all().select_related('course').select_related('publisher')\
            .annotate(course_name=F('course__name'))

        if 'course_ids' in params:
            course_ids = params['course_ids']
            qs = qs.filter(course_id__in = course_ids)


        if 'course_id' in params:
            qs = qs.filter(course_id = params['course_id'])

        if 'starttime' in params:
            starttime = params['starttime']
            qs = qs.filter(starttime__gte = parse_datetime(json.loads(starttime)))


        if 'endtime' in params:
            endtime = params['endtime']
            qs = qs.filter(endtime__lte = parse_datetime(json.loads(endtime)) +
                                          timedelta(hours=23,minutes=59,seconds=59))


        if 'publisher_id' in params:
            publisher_id = params['publisher_id']
            qs = qs.filter(publisher_id = publisher_id)

        qs = qs.values('id','course_id','course_name','starttime','endtime',
                       'publisher_id','publisher__last_name','desc').order_by('-id')

        pgnt = Paginator(qs, pagesize)

        try:
            retObj = list(pgnt.page(pagenum))
        except EmptyPage:
            return [], 0

        return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}


    @staticmethod
    def add(data,publisher_id):
        Lesson.objects.create(course_id=data['course_id'],
                                publisher_id=publisher_id,
                                desc=data['desc'],
                                starttime=parse_datetime(data['starttime']),
                                endtime=parse_datetime(data['endtime']))

        return {'retcode': 0}



    @staticmethod
    def modify(rid,data):
        Lesson.objects.filter(id=rid)\
                      .update(course_id=data['course_id'],
                                desc=data['desc'],
                                starttime=parse_datetime(data['starttime']),
                                endtime=parse_datetime(data['endtime']))
        return {'retcode': 0}


# 培训班
class Training(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    # 有哪些课
    courselist = models.TextField(null=True, blank=True)

    desc = models.CharField(max_length=1500, null=True, blank=True)
    # 展示优先级
    display_idx = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "sq_training"

    @staticmethod
    def list(pagenum,pagesize):

        return comm_list(Training,pagenum,pagesize)


    @staticmethod
    def add(data):
        Training.objects.create(name=data['name'],
                                courselist=data['courselist'],
                                desc=data['desc'],
                                display_idx=data['display_idx'])

        return {'retcode': 0}

    @staticmethod
    def modify(rid,data):
        Training.objects.filter(id=rid)\
                      .update(name=data['name'],
                              courselist=data['courselist'],
                              desc=data['desc'],
                              display_idx=data['display_idx'])
        return {'retcode': 0}


    @staticmethod
    def getcourseidlistbyid(training_id):

        training = Training.objects.get(id=training_id)
        courselist = json.loads(training.courselist)
        cousreidlist = [c['id'] for c in courselist]

        return cousreidlist

# 培训班期
class TrainingGrade(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    # 所属培训班
    training = models.ForeignKey(Training, blank=False, related_name='Grade',on_delete=models.PROTECT)

    desc = models.CharField(max_length=1500, null=True, blank=True)
    display_idx = models.PositiveSmallIntegerField(default=0) # 展示优先级

    class Meta:
        db_table = "sq_training_grade"

    @staticmethod
    def list(pagenum,pagesize):

        qs = TrainingGrade.objects.select_related('training').all()

        qs = qs.order_by('display_idx').annotate(trainingname=F('training__name'))\
            .values('id','name','desc','display_idx','trainingname','training__id')

        pgnt = Paginator(qs, pagesize)

        # retObj = {'total':pgnt, 'content':pgnt.page(pagenum)}
        try:
            retObj = list(pgnt.page(pagenum))
        except EmptyPage:
            return [], 0

        return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}


    @staticmethod
    def add(data):
        TrainingGrade.objects.create(name=data['name'],
                                     training_id=data['training_id'],
                                     desc=data['desc'],
                                     display_idx=data['display_idx'])

        return {'retcode': 0}

    @staticmethod
    def modify(rid,data):
        TrainingGrade.objects.filter(id=rid)\
                      .update(name=data['name'],
                              training_id=data['training_id'],
                              desc=data['desc'],
                              display_idx=data['display_idx'])
        return {'retcode': 0}

# 学生
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student',on_delete=models.PROTECT)
    realname = models.CharField(max_length=30, db_index=True)
    # 所属培训班
    training = models.ForeignKey(Training,  related_name='traningstudents',on_delete=models.PROTECT)
    # 所属培训班期
    traininggrade = models.ForeignKey(TrainingGrade,  related_name='traninggradestudent',on_delete=models.PROTECT)
    # 入学时间
    startcoursedate = models.DateField(db_index=True)
    # # 学哪些课
    # courselist = models.TextField(null=True, blank=True)
    # 是否已经毕业
    graduated = models.BooleanField(default=False,db_index=True)
    # 是否有效
    active =  models.BooleanField(default=True)

    desc = models.CharField(max_length=1500, null=True, blank=True)



    @staticmethod
    def _getcheckinlessons(courseidlist):

        curTime = datetime.now()
        begin = curTime  - timedelta(minutes=30)
        end   = curTime  + timedelta(minutes=10)

        clessons = Lesson.objects.filter(course_id__in=courseidlist,
                                          starttime__gte=begin,
                                          starttime__lte=end) \
                    .select_related('course')\
                    .values('id','course__name','starttime','endtime','desc')
        return list(clessons)

    @staticmethod
    def getstudentcheckinlessons(studentid):

        try:
            student = Student.objects.select_related('training').get(id=studentid)
        except Student.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的学生不存在'.format(studentid)
            }

        courseidlist = Training.getcourseidlistbyid(student.training.id)
        slessons = Student._getcheckinlessons(courseidlist)

        lessonidlist = [one['id'] for one in slessons]

        # 去掉已经签到的课
        checkedLessonids = StudentCheckin.objects.filter(lesson_id__in=lessonidlist,student_id=studentid)\
            .values_list('lesson_id', flat=True)
        finalslessons = [one for one in slessons if one['id'] not in checkedLessonids]


        return {
            'retcode': 0,
            'clessons' : finalslessons
        }

    @staticmethod
    def _getlessonschedule(courseidlist):


        todayTime = datetime.now()
        begin = todayTime.replace(hour=0, minute=0,second=0,microsecond=0)
        end   = begin  + timedelta(weeks=1)
        slessons = Lesson.objects.filter(course_id__in=courseidlist,
                                          starttime__gte=begin,
                                          starttime__lte=end) \
                    .select_related('course')\
                    .values('id','course__name','starttime','endtime','desc')
        return list(slessons)

    @staticmethod
    def getstudentscheduledlessons(studentid):

        try:
            student = Student.objects.select_related('training').get(id=studentid)
        except Student.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的学生不存在'.format(studentid)
            }

        courseidlist = Training.getcourseidlistbyid(student.training.id)
        slessons = Student._getlessonschedule(courseidlist)



        return {
            'retcode': 0,
            'slessons' : slessons
        }

    @staticmethod
    def getone(studentid):
        try:
            student = Student.objects.get(id=studentid)
        except Student.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的学生不存在'.format(studentid)
            }

        info = {
            'realname':student.realname,
            'training_name':student.training.name,
            'traininggrade_name':student.traininggrade.name,
            'startcoursedate':student.startcoursedate,
            'graduated':student.graduated
        }

        return {
            'retcode': 0,
            'info': info
        }




    @staticmethod
    def getOneClassStudent(classid):
        qs = Student.objects.filter(traininggrade_id =classid).\
            values('id','realname').order_by('-id')
        return list(qs)


    @staticmethod
    def list(pagenum,pagesize,params):

        qs = Student.objects.all() \
                .select_related('training') \
                .select_related('traininggrade') \
                .select_related('user') \
                .annotate(trainingname=F('training__name')) \
                .annotate(traininggradename=F('traininggrade__name')) \
                .annotate(username=F('user__username')) \
                .annotate(userid=F('user__id'))


        if 'training_id' in params:
            qs = qs.filter(training_id = params['training_id'])
        if 'traininggrade_id' in params:
            qs = qs.filter(traininggrade_id =params['traininggrade_id'])
        if 'name' in params:
            qs = qs.filter(realname =params['name'])


        qs = qs.values('id','username','userid','realname','training_id','trainingname',
                       'traininggrade_id','traininggradename',
                       'startcoursedate','graduated','desc','active').order_by('-id')

        pgnt = Paginator(qs, pagesize)

        # retObj = {'total':pgnt, 'content':pgnt.page(pagenum)}
        try:
            retObj = list(pgnt.page(pagenum))
        except EmptyPage:
            return [], 0

        return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}


    @staticmethod
    def add(data):
        username    = data['username']
        realname    = data['realname']
        try:
            if User.objects.filter(username=username).exists():
                return {'retcode': 1, 'reason': u'登录名 %s 已经存在'%username}

            with transaction.atomic():
                new_user = User.objects.create(
                    username  = username,
                    usertype  = settings.USER_TYPE.STDUENT,
                    password  = make_password(data['password']),
                    last_name = realname,
                    phonenumber  = '',
                    idcardnumber = '',
                    email        = '',
                )

                student = Student(user=new_user,
                                  realname=realname,
                                  desc=data['desc'],
                                  training_id=data['training_id'],
                                  traininggrade_id=data['traininggrade_id'],
                                  startcoursedate=parse_datetime(data['startcoursedate']))

                student.save()

                return {'retcode': 0, 'id': student.id}

        except IntegrityError:
            err = traceback.format_exc()
            model_logger.error(err)
        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            return {'retcode': 1, 'reason': err}

    @staticmethod
    def modify(studentid,data):
        try:
            student = Student.objects.get(id=studentid)
        except Student.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的学生不存在'.format(studentid)
            }

        for param in ['realname',  'desc', 'training_id','traininggrade_id','graduated']:
            if param in data:
                setattr(student, param, data[param])

        if 'startcoursedate' in data:
            student.startcoursedate = parse_datetime(data['startcoursedate'])

        try:
            with transaction.atomic():
                student.save()

                # 可能要更新user表里面的名字
                tu_changed = False
                if 'realname' in data:
                    student.user.last_name = data['realname']
                    tu_changed = True
                if 'username' in data:
                    student.user.username = data['username']
                    tu_changed = True
                if tu_changed:
                    student.user.save()


        except IntegrityError as e:
            return {'retcode': 1, 'reason': str(e)}
        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            raise

        return {'retcode': 0}

    class Meta:
        db_table = "sq_student"
        index_together = ("user", "graduated","active")


    @staticmethod
    def changePasswordByStudent(userid,oldpassword,newpassword):
        try:
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return {'retcode': 1, 'reason': u'没有此用户'}

        if not check_password(oldpassword, user.password):
            return {'retcode': 1, 'reason': u'原密码错误'}

        user.password = make_password(newpassword)

        try:
            user.save()
        except :
            return {'retcode': 1, 'reason': u'修改用户密码失败'}

        return {'retcode': 0}


    @staticmethod
    def deleteOne(studentid):

        try:
            student = Student.objects.get(id=studentid)
        except Teacher.DoesNotExist:
            return {
                'retcode': 1,
                'reason': u'id 为`{}`的学生不存在'.format(studentid)
            }

        try:
            with transaction.atomic():
                student.delete()

                # 同时要删除user表里对应的
                student.user.delete()

        except Exception:
            err = traceback.format_exc()
            model_logger.error(err)
            raise

        return {'retcode': 0}


# 学生签到记录
class StudentCheckin(models.Model):
    student = models.ForeignKey(Student, related_name='student_checkin',on_delete=models.PROTECT)
    # 课时
    lesson = models.ForeignKey(Lesson,  related_name='checkin_students',on_delete=models.PROTECT)
    # 签到时间
    checkintime = models.DateTimeField(default=now)

    class Meta:
        db_table = "sq_student_checkin"
        unique_together = (("student", "lesson"),)



    @staticmethod
    def addOne(studentid,lessonid):



        try:
            StudentCheckin.objects.create(
                student_id=studentid,
                lesson_id=lessonid
            )
        except IntegrityError:
            return {'retcode': 2,'reason':u'该课已经签到过了'}


        return {'retcode': 0}


    @staticmethod
    def listRecords_by_lesson(lessonid):

        qs = StudentCheckin.objects.all().select_related('student').filter(lesson_id = lessonid)

        qs = qs.values('id','student__realname','student__traininggrade_id','student__id')\
            .order_by('student__traininggrade_id','id')


        return {'retcode': 0, 'retlist': list(qs), }

    @staticmethod
    def listRecords_by_student(pagenum,pagesize,params,studentid=None):

        qs = StudentCheckin.objects.all().select_related('lesson__course')\
            .annotate(lessonname=F('lesson__course__name'),lessondesc=F('lesson__desc'))

        if studentid:
            qs = qs.filter(student_id = studentid)


        if 'starttime' in params:
            starttime = params['starttime']
            qs = qs.filter(checkintime__gte = parse_datetime(json.loads(starttime)))


        if 'endtime' in params:
            endtime = params['endtime']
            qs = qs.filter(checkintime__lte = parse_datetime(json.loads(endtime)) +
                                          timedelta(hours=23,minutes=59,seconds=59))


        qs = qs.values('id','checkintime','lessonname','lessondesc',
                       'lesson__starttime','lesson__course_id','lesson__id').order_by('lesson__course_id','-id')

        pgnt = Paginator(qs, pagesize)

        try:
            retObj = list(pgnt.page(pagenum))
        except EmptyPage:
            return [], 0

        return {'retcode': 0, 'retlist': retObj, 'total': pgnt.count}