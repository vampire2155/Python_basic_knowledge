#异常处理。使用 try ... except 进行异常管理       异常是类，一定要继承父类

# while True:
#     num = input('Please input a value:')
#     try :
#         print ('100 / %s = %s' % (num,100/int(num)))
#     except ZeroDivisionError:
#         print ('分母不能为零，请重新输入！')
#     except Exception as error:
#         print ('请重新输入！',error)


'''
#自定义异常  ：可以自己定义异常
#定义名称太长的类
class NameTooLongError(Exception):
    error = 'name is long'
    print ('NameTooLongError')
    def methFun(self):
        pass
#定义名称太短的类
class NameTooShortError(Exception):
    print ('NameTooShortError')

def inputName():
    name = input('Please input a name:')
    if len(name) > 10:
        raise NameTooLongError
    elif len(name) < 5:
        raise NameTooShortError
try:
    inputName()
except NameTooLongError as e:
    print ('input name is too long,Please input again!',e.error)
    e.methFun()
except NameTooShortError:
    print('input name is too short,Please input again!')
'''

'''
#异常处理的原则，如果有具体的异常，则使用具体的异常，如果没有则使用except Exception  。
import traceback
num = input('input a number:')
while True:
    try:#捕获下面语句的异常
        res = '100 / %s = %s' % (num, 100.0/int(num))
        print (res)
    except ZeroDivisionError:#一种已知的异常，其他异常不能处理
        print('除数不能为0 ，重新输入！')

    except ValueError as error:
        print('除数为数字！',error)

    except Exception :#未知的异常
        print('除数不能为浮点数！')

    except: #except Exception简写
        print('异常了，请处理异常.\n',traceback.format_exc())#详细的报错信息

    break
'''

# 自定义异常   ---需要继承Exception() 父类
class NameTooLongError(Exception):
    err = 'name is out of range.'
    print('NameTooLongError')
    def methFun(self):
        return self.err

#自定义异常-----name 过短异常--继承
class NameTooShortError(Exception):
    err = 'name is out of range.'
    print('NameTooShortError')
    def methFun(self):
        return self.err

def inputName():
    name = input('请输入用户名：')#5-10
    if len(name) > 10:
        raise NameTooLongError #自定义的异常要自行抛出
    elif len(name) < 5:
        raise NameTooShortError

try:
    inputName()
except NameTooShortError as e:
    print('您输入的用户名太短！',e.methFun())
except NameTooLongError as e:
    print('您输入的用户名太长！',e.methFun())





