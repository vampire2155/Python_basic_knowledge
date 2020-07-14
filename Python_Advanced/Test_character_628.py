#string 转 数字   ---ord()函数
# print (ord('折'))

#数字  转  string  ---chr()函数 参数只能是 正整数
# print (chr(12345))  #打印结果为 〹

#怎样把一个a.txt文件中的内容复制出来并另存为 b.txt
#先读取出来，然后再保存在b.txt中
'''
# 方法一：
data = ""   #先定义一个空字符串变量，用来接收 读取出来的内容
#先把内容全部读取出来并存入data变量中
with open('a.txt','r',encoding='utf8') as fo:
    data = fo.read()

#然后把变量data中的内容写入到b.txt中 ,，需要注意的是读和写的时候的编码必须一致，否则写入的就可能是乱码。
with open('b.txt','w',encoding='utf8') as fo:
    fo.write(data)

#上述方法可行，但是读和写的时候分别进行了一个编码转换，多次一举了。所以下面的方法更加 简单快捷
#方法二：  读 和 写的时候都选用 二进制方式（bytes），因为文件在计算机中就是以二进制存储的。所以比方法一省去了转换的过程。
data = ""
with open('a.txt','rb') as fo:  # rb表示以 二进制方式 读取
    data = fo.read()
with open('b.txt','wb') as fo:  # wb表示以 二进制方式 写入
    fo.write(data)
'''

'''
解压该压缩包，里面 包含了两个文件。 一个叫 'gbk编码.txt',该文件是gbk编码的。另一个文件叫 'utf8编码.txt', 该文件是utf8编码的。
两个文件里面的内容都包含中文。
要求大家编写一个python程序，该程序做到以下2点:
1. 将两个文件内容读出， 合并内容到一个字符串中，并能用print语句将合并后的内容正确显示  
2. 然后，程序用中文提示用户“请输入 新文件的名称”，用户输入文件名可以包含中文.将上面合并后的内容存储到一个新文件中，以utf8格式编码。
新文件的文件名就是上面用户输入的名字。

str = ''
with open('utf8编码.txt',encoding='utf8') as utf,open('gbk编码.txt',encoding='gbk') as gbk:
    str = f'{utf.read()},{gbk.read()}'
print (str)
fileName = input("请输入 新文件的名称:")
with open(f'{fileName}.txt','w',encoding='utf8') as new_file:
    new_file.write(str)
'''
# （1）第一种形式——直接调用
# def Maker(name):
#     num=100
#     def func1(weight,height,age):
#         weight+=1
#         height+=1
#         age+=1
#         print(name,weight,height,age)  #在此处调用了外部函数Maker()中的变量 name 。
#
#     func1(100,200,300)  #在内部就直接调用“内部函数”
# Maker('feifei')         #调用外部函数，输出 feifei 101 201 301


# （2）第二种形式——返回函数名称
# def Maker(name):
#     num=100
#     def func1(weight,height,age):
#         weight+=1
#         height+=1
#         age+=1
#         print(name,weight,height,age)
#     return func1  #此处不直接调用，而是返回 函数名（Python中一切皆对象）
# a=Maker('feifei') #调用包装器，这里相当于把 feifei赋值给 name变量；然后把函数Maker()的返回值 func1 赋值给 变量--> a . name = 'feifei'  ; a = func1.
# a(100,200,300)    #调用内部函数。因为 此时 a = func1 .所以a(100,200,300) == func1(100,200,300)

'''
def Maker(step):
    num=1
    def fun1():  #内部函数
        nonlocal num  #nonlocal关键字的作用和前面的local是一样的，如果不使用该关键字，则不能再内部函数改变“外部变量”的值
        num=num+step  #改变外部变量的值（如果只是访问外部变量，则不需要使用nonlocal）
        print(num)
    return fun1

j=1
func2=Maker(3)  #调用外部函数。外部函数Maker()的返回值是fun1
while(j<5):
    func2()    #调用内部函数4次 输出的结果是 4、7、10、13
    j+=1
# 从上面的例子可以看出，外部装饰器函数的局部变量num=1、以及调用装饰器Maker(3)时候传入的参数step=3都被记忆了下来，所以才有1+3=4、4+3=7、7+3=10、10+3=13.
# 从这里可以看出，Maker函数虽然被调用了，但是它的局部变量信息（step=3）却被保存了下来，这就是“闭包”的最大的作用——保存局部信息（step=3）不被销毁。
'''

#现已实现以下功能 my_log、my_name、my_shopping_mall 函数, 账户名密码来自字典变量,需要通过输入验证是否正确
# 要求编写装饰器， 计算 从输入用户名密码、my_log、my_name、my_shopping_mall 三个函数执行一次到退出所需要的时间。my_log等三个函数需要依赖token。
from random import randint
import time

startTime = time.time()
print(f'startTime:{startTime}')
input_usrname = input('输入用户名>>>')
input_psd = input('输入密码>>>')
user_dict = {# 存用户名和密码
            'username':'123',
            'password':'123456'
            }
def get_token(func):
    def auth(*args):
        if input_usrname == user_dict['username'] and input_psd == user_dict['password']:
            a = randint(1111, 99999)
            token = 'xxxacbx2xdegcgdxx'.join(str(a))
            print (f'The token value is:{token}.')
        else:
            print ('用户名或者密码错误！')
        func(*args)  #这条语句应该放在获取 token之后，因为做其他操作需要先获取token值。  *args 可变数量参数。

    return auth

@get_token   #这一个操作相当于 my_log = get_token(my_log)
def my_log():
    print ('this is my_log')

@get_token
def my_name(name):
    print ('欢迎登陆',name)

@get_token
def my_shopping_mall():
    print ('商城购物')

while True:
    choose_num = input('\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项(输入 q 退出)>>>')
    if choose_num == 'q' or choose_num == 'Q':
        break
    elif choose_num == '1':
        my_log()
    elif choose_num == '2':
        my_name('张三')
    elif choose_num == '3':
        my_shopping_mall()
    else:
        print ('输入不合法。')
endTime = time.time()
print (f'endTime:{endTime}')
totalTime = endTime - startTime
print (f'耗时：{totalTime}')



