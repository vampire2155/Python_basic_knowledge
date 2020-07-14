# -*- coding: UTF-8 -*-
# 5-24日布置的作业   学习内容：python基础之初始函数和对象的方法
'''
现有一个游戏系统的日志文件，记录内容的字符串 的格式 如下所示
A girl come in, the name is Jack, level 955;
其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。
其它部分可能都是会变化的，比如，可能是下面这些
A old lady come in, the name is Mary, level 94454
A pretty boy come in, the name is Patrick, level 194
请大家实现一个函数，名为getName，如下所示
def getName(srcStr):
    函数体
该函数的参数srcStr 是上面所描述的格式字符串（只处理一行），该函数需要将其中的人名获取出来，并返回
比如 调用 getName('A old lady come in, the name is Mary, level 94454')
返回结果应该是 'Mary'
'''
#代码实现如下
'''
def getName(srcStr):
    New_srcStr = srcStr.split('the name is')[1]
    result = New_srcStr.lstrip().split(',')  #去掉左边的空格，然后再使用逗号分隔
    return result[0]
res = getName('A old lady come in, the name is Mary, level 94454')
res1 = getName('A pretty boy come in, the name is Patrick, level 194')
res2 = getName('A girl come in, the name is Jack, level 955')
print ('res的结果为:',res)
print ('res1的结果为:',res1)
print ('res2的结果为:',res)
'''


log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0	
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0	
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0	
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0	
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0	
f20180111090619/i_3BKlsRaZ.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156330575626044	image/jpeg	0	
f20180111090619/i_5XboXSKh.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156329453409855	image/jpeg	0	
f20180111090619/i_6DiYSBKp.jpg	74017	FrYG3icChRmFGnWQK6rYxa88KuQI	15156329461803290	image/jpeg	0	
f20180111090619/i_76zaF2IM.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156334738356648	image/jpeg	0	
f20180111090619/i_B6TFYjks.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156329464034474	image/jpeg	0	
f20180111090619/i_N9eITqj3.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156330419595764	image/jpeg	0	
f20180111090619/i_QTSNWmA6.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156333104224056	image/jpeg	0	
f20180111090619/i_XdHcAfh1.jpg	56479	FjLQIQ3GxSEHDfu6tRcMylK1MZ05	15156334227270309	image/jpeg	0	
f20180111090619/i_Xyy723MU.jpg	50076	FsfZpQzqu084RUw5NPYW9-Yfam_R	15156334229987458	image/jpeg	0	
f20180111090619/i_d8Go0EOv.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156334736228515	image/jpeg	0	
f20180111090619/i_diuHmX53.jpg	40591	FuTx1pw4idbKnV5MSvNGxCA5L470	15156333878320713	image/jpeg	0	
f20180111090619/i_qQKzheSH.jpg	55858	Fj0A3i8V7fzzOiPQFL79ao15hkN9	15156329456666591	image/jpeg	0	
f20180111090619/i_rHL5SYk8.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156336509742181	image/jpeg	0	
f20180111090619/i_xZmQxUbz.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156333240603466	image/jpeg	0	
f20180111090619/i_zBDNgXDv.jpeg	73616	FlgNwq8lypgsxrWs_ksrS_x47SQV	15156334232887875	image/jpeg	0	
f20180111090619/j_4mxbEiVh.json	2990	Fpq-3yl3Yr1CadNrJVSDnpeRhQtT	15156331445226898	application/json	0	
f20180111090619/j_i1K74768.json	3042	Fl5PpDw1TsZXMuhoq1RUrOeGZ6br	15156335067090003	application/json	0	
f20180111095839/i_Q7KMKeda.png	518522	Fl-yB1_ruL2uxZN9k7DjB62h9dYH	15156359599713253	image/png	0	
f20180111095839/j_5DpqHolV.json	184	FoYvi7cmSrzuVjUgCRzW5kU95SVo	15156359719719064	application/json	0	
f20180111100442/i_No8kToIV.jpg	48975	Fu1cw3f--5Vpz9kLGeJfvljhCtyZ	15156364349642377	image/jpeg	0	
f20180111100442/i_P1bkvSeg.jpg	68200	FvYe8vi46TjUKhEy_UwDqLhO6ZsW	15156363800690634	image/jpeg	0	
f20180111100442/i_T1AulKcD.jpg	52641	Fj2YzvdC1n_1sF93ZZgrhF3OzOeY	15156364021186365	image/jpeg	0	
f20180111100442/i_X8d8BN07.jpg	50770	FivwidMiHbogw77lqgkIKrgmF3eA	15156363969737156	image/jpeg	0	
f20180111100442/i_g0wtOsCX.jpg	76656	Fmtixx0mP9CAUTNosjLuYQHL6k0P	15156363448222155	image/jpeg	0	
f20180111100442/i_h5OT9324.jpg	72672	FvbIqPLTh2cQHTIBv2akUfahZa_Z	15156364401354652	image/jpeg	0	
f20180111100442/i_he8iLYI6.jpg	49399	FjeJvwjwhU-hKZsq66UoBg9_tEJs	15156363907932480	image/jpeg	0	
f20180111100442/i_kg29t7Pp.jpg	76293	FuYj__sSeEN7AsXMbxO24Z8Suh8d	15156364156384686	image/jpeg	0	
f20180111100442/i_oz1YoBI1.jpg	75620	FkY3xsUMwOI01zgoH1iXXgiQeq6I	15156364089112904	image/jpeg	0	
f20180111100442/i_xrOT98on.jpg	50021	Fql7ookM1Rc6V7VairKAfnKe-o9w	15156363856357316	image/jpeg	0	
f20180111135114/i_Zqt8Tmoe.png	161629	FlELw59_mV3VqDBLyu1BKN4fIWnx	15156500155209863	image/png	0	
f20180111135114/j_uhHoMXKq.json	159	FrypljwAr2LgoLAePBNTUYTUAgDt	15156500200488238	application/json	0	
f20180111142119/i_s83iZ2GR.png	92278	Fns8tdh3JCkRmfE_COYEu4o8w03E	15156517082371259	image/png	0	
f20180111142119/j_0g45JRth.json	159	Fq1rFwdRguYRXrp61nGZ5TsUG1V-	15156517143375596	application/json	0	
f20180111144306/i_yE5TC84E.png	139230	Fjf61ymabEnEvnr5ZMHFjXGCrYlP	15156530038824150	image/png	0	
f20180111144306/j_OF4WVtSH.json	159	FqwkKcxfo8jd0jFUyuH4X2CrnE9q	15156530083419530	application/json	0	
f20180111150230/i_KtnER4g3.png	120044	FuwOWdrqzcr2-UScem-LzEMgMezs	15156541734892258	image/png	0	
f20180111150230/j_xMSUEejY.json	158	FjJr_4deMqFphGaptm-2Pa6wwRP2	15156541771989216	application/json	0	
f20180111151741/i_JuSWztB3.jpg	92506	FrIjRevHSi6xv4-NQa2wrHu5a1zQ	15156550875370965	image/jpeg	0	
f20180111153550/i_9wWzVenl.gif	769872	FvslKY9JUaCQm-lu02E34tvAP_oG	15156561674621628	image/gif	0			
'''
#题目要求：   5-25日布置，学习内容：python基础之字符串的格式化循环语句与注释
# 1.下面的log变量记录了云服务器上 当天上传的文件信息
# 其中第一列是文件名，第二列是文件大小
# 请编写一个程序，统计出不同类型的 文件的大小总和
# 比如：
# jpeg  9988999
# json   324324
# png   2423233
'''
def get_fileSize(file_suffix,file_size):
    for one in fileToalSize:
        if one[0] == file_suffix:
            one[1] += file_size
            return
    fileToalSize.append([file_suffix, file_size])
    return
fileToalSize = []
i = 1
while i <=len(log.split('\n'))-2:
    file_suffix = log.split('\n')[i].split(' ')[0].split('.')[1].split('	')[0]
    file_size = log.split('\n')[i].split(' ')[0].split('.')[1].split('	')[1]
    i +=1
    get_fileSize(file_suffix,int(file_size))
for one in fileToalSize:
    print ('文件后缀名为'+ str(one[0])+'的文件总大小为:'+str(one[1]))
'''

'''
请实现一个程序，实现如下需求点： 5-25日布置，学习内容：python基础之字符串的格式化循环语句与注释
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格） 
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''

'''
# 代码实现如下
#方法一：这个是其他同学写的代码
input_info = input('输入用户年龄信息：')
Stu_info = input_info.replace(' ','').split(';')
del Stu_info[-1]
for one in Stu_info:
    name,age = one.split(',')   #列表赋值法
    print('{:<20}:{:0>2};'.format(name,age))


#方法二：  这个是老师提供的答案
inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input
    if ',' not in one:
        continue
    name, age = one.split(',')
    name = name.strip()
    age = age.strip()
    #  check is age digit
    if not age.isdigit():
        continue
    age = int(age)
    print('%-20s :  %02d' % (name, age))


#方法三： 这个是我写的代码
info = input("Please input students' info:")
j = 0
i = len(info.split(';'))-1 #因为每次输入结尾有一个分号，切割完以后 会有一个空元素，所以需要把这个空元素排除掉。
while j <i:
    name = info.split(';')[j].split(',')[0].strip()
    age = info.split(';')[j].split(',')[1].strip()
    j += 1
    # print ('{:<20}'.format(name) + ':' + '{:0>2}'.format(age))  #这种写法需要优化
    print ('{:<20}:{:0>2}'.format(name,age))
    print (f'{name:<20}:{age:0>2}')
'''
'''
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
请按下面算法的思路实现函数：
1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面   

# 实现如下：
aList = [-1, 9.3, 7, 22, 200,0]
def mySort(aList):
    bList = []
    while len(aList) > 0:
        for one in aList:
            if one == min(aList):
                bList.append(one)
                aList.remove(one)
    return bList
print (mySort(aList))

#题目要求：使用  假设法  对一个列表中的元素进行从小到大的排序并输出
aList = [10, 9, 7, 22, 200,0]
def mySort(aList):
    bList = []
    while len(aList) > 0:
        #假设一个最小值,（假设第一个元素是最小值）
        minindex = 0
        minData = aList[0]
        i = 0
        for one in aList:
            if aList[0] > one:  #如果假设的最小值 比其他元素的值大
                minData = one   #则把其他元素的值赋给 最小值
                minindex = i  #而且需要把其他元素的 index也要赋给 当初家设置的最小值的index
            i += 1
        bList.append(minData)
        del aList[minindex]
    return bList
print (mySort(aList))
'''

'''
现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格
现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示
name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数 

fileDir = r'G:\Python_scripts\file1.txt'
with open(fileDir) as file_Obj:
        read_res = file_Obj.read().splitlines()
for one in read_res:
        salary = one.replace(' ','').split(';')[1].split(':')[1]
        name = one.replace(' ','').split(';')[0].split(':')[1]
        tax = int(int(salary)*0.1)
        income = int(int(salary)*0.9)
        result = f'name:{name:<10}; salary:{salary:>10}; tax:{tax:>10}; income:{income:>10}\n'
        with open(r'G:\Python_scripts\file2.txt','a') as file_salary:
                file_salary.write(result)
'''

# 下面的代码为老师提供的答案，此代码的优点在于，当存在不合理的数据时（即数据不完整），代码执行不会报错。
# inFileName = r'G:\Python_scripts\file1.txt'
# outFileName = r'G:\Python_scripts\file2.txt'
# with open(inFileName) as ifile, open(outFileName, 'w') as ofile:
#         beforeTax = ifile.read().splitlines()
#         for one in beforeTax:
#                 if one.count(';') != 1:  # ensure valid
#                         continue
#                 namePart, salaryPart = one.split(';')
#                 if namePart.count(':') != 1:  # ensure valid
#                         continue
#                 if salaryPart.count(':') != 1:  # ensure valid
#                         continue
#                 name = namePart.split(':')[1].strip()
#                 salary = int(salaryPart.split(':')[1].strip())
#                 income = int(salary * 0.9)
#                 tax = int(salary * 0.1)
#                 outPutStr = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(name, salary, tax,income)
#                 print (outPutStr)
#                 ofile.write(outPutStr + '\n')

'''
5-31日课程内容： 字典及再识函数
现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下 ，
('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),
每一行记录保存了学生的一次签到信息。
每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号
要求大家实现下面的函数。其中参数fileName 为 数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：
key 是各个学生的id号， value是 该学生的签到信息,其中value，里面保存着该学生所有签到的信息
其中每个签到的信息是字典对象，有两个元素： key 是lessonid的 记录课程id，key是checkintime的 记录签到时间
比如，对于上面的示例中的3条记录，相应的返回结果如下：
{
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],   
    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ],  
}
'''
#使用字典实现的代码如下：
# from pprint import pprint
# fileName = r'G:\Python_scripts\0005_1.txt'
# infoDict = {}
# def putInfoToDict(fileName):
#     with open(fileName) as fo:
#         fileList = fo.read().replace(';',',').replace('(','').replace(')','').splitlines()
#         for one in fileList:
#             info = one.strip().split(',')
#             checkintime,lessonid,userId = info[0].replace("'",''),int(info[1].strip()),int(info[2].strip())
#             temp = {'lessonid':lessonid,'checkintime':checkintime}
#             if userId not in infoDict:   #开始时字典是空的
#                 infoDict[userId] = []
#             infoDict[userId].append(temp)
#         return infoDict
# putInfoToDict(fileName)
# pprint(infoDict)
#

#计算 2的n次的值  有多重方法：1、使用运算符 **    2、使用math.pow()函数    3、使用for 循环，列表   4、使用自定义函数
# aList = [2,2,2,2,2,2,2,2]
# sum = 1
# for one in aList:
#     sum = one * sum
# print (sum)

#使用math.pow()函数
import math
# print (pow(2,8))

#使用运算符 **
# print (2**8)

#使用自定义函数  计算 x的y次方的值
# def power(x,y):
#     n = 0
#     res = 1
#     while n < y:
#         res = x * res    #n = 0 --> res = 5*1 ; n=1 --> res= 5*5 ; n = 2 --> res = 5 * 25
#         n +=1
#     return res
# print (power(-5,3))


# str = "('a','11',2)"
# def strTurntoList(str):
#     aList = str.replace('"','').replace('(','').replace(')','').replace("'",'').split(',')
#     return aList
# print (strTurntoList(str))

#统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
#思路：方法一：使用for循环
# aList = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# bList = []
# cList = []
# for one in aList:
#     if one > 0:
#         bList.append(one)
#     elif one < 0:
#         cList.append(one)
# print (f'正数的个数为：{len(bList)}；负数的个数为：{len(cList)}')
# print ('正数的个数为：{}；负数的个数为：{}'.format(len(bList),len(cList)))

#方法二：使用列表生成式 方法
# aList = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# bList = [one for one in aList if one >0]
# cList = [one for one in aList if one <0]
# print ('正数的个数为%s' % len(bList))
# print ('负数的个数为%s' % len(cList))

#已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]
# str = 'hello_world_yoyo'
# print (str.split('_'))

#已知一个数字为 1，如何输出“0001”
# str = '1'
# print ('{:0>4}'.format(str))

#已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到： [3, 5, 1, 7]
# aList = [1, 3, 5, 7]
# aList.insert(3,aList[0])  #不能把这个结果赋给一个变量，如果赋给一个变量，这个变量的值为 None
# print (aList[1:])


#打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数 字立方和等于该数本身。例如：153 是一个"水仙花数"，
# 因为 153 = 1的三次方＋ 5的三次方＋3的三次方。
'''
如下这种方法，执行结果中多了一个370 ，经过debug发现当 i= 370时 for执行完 3 和 7 时，i 和 s已经相等，即if 条件已经成立，
所以，会把370给append到sxh列表中.而此时for循环还没有遍历完，所以会继续执行，此时3,7,0三个数的三次方和就是370，所以又会append一次。
所以，sxh列表中会有两个 370 。 解决方法，需要在if i == s: 里面再加一个判断 if int(j) != 0:
'''
# sxh = []
# for i in range(100, 1000):
#     s = 0
#     m = list(str(i))    #m 的值为：['1', '0', '0'] ['1', '0', '1'] ......
#     for j in m:
#         s += int(j)**len(m)    #把列表 m 中的各个元素的3次方的和相加
#         if i == s:
#             if int(j) != 0:
#                 sxh.append(i)
# print("100-999 的水仙花数：%s" % sxh)

#方法二：  使用 幂运算 符进行计算。
# sxh = []
# for i in range(100, 1000):
#     s = 0
#     m = list(str(i))    #m 的值为：['1', '0', '0'] ['1', '0', '1'] ......
#     if i == (int(m[0])**3 + int(m[1])**3 + int(m[2])**3):
#             sxh.append(i)
# print("100-999 的水仙花数：%s" % sxh)


'''
题目要求如下：
如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。 
例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余 3 个数相加， 1+2+3=6。
第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28 外，其余 5 个数相加，1+2+4+7+14=28。 
那么问题来了，求 1000 以内的完全数有哪些？
'''
#方法一：这个是我写的 ，列表 yz = [] 完全没有必要
# wqs = []
# yz = []  #这个列表完全没有必要加，可以查看方法二的写法。
# for i in range(1,1000):
#     for j in range(1,i):  #
#         if i%j == 0:
#             yz.append(j)
#     # del yz[-1] #需要全部计算完才能删除掉最后一个元素，所以不能写在for循环里面。
#     sum = 0
#     for x in yz:
#         sum +=x
#     if sum == i:  #需要全部加完再去判断是否相等，而不是 每加一次判断一次。所以这个条件不能写在 for循环里面，得写在for循环外面。
#         wqs.append(i)
#     yz.clear()  #这一步很重要，如果不清除的话，会在原来的基础上一直append。所以，需要每判断完一个数，就需要清除一次。
# print (f'1000以内的完全数为：{wqs}')

#方法二：
# a = []
# for i in range(1, 1000):
#     s = 0
#     for j in range(1, i):
#         if i % j == 0:  #if i % j == 0 and j < i: 原来的语句是这一条，但是这个 j<i 没有必要。
#             s += j
#     if s == i:
#         a.append(i)
# print("1000 以内完全数：%s" % a)


'''
已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
 按从小到大排序 
 按从大到小排序 
 去除重复数字 
'''
# aList = [1, 3, 6, 9, 7, 3, 4, 6]
# bList = list(set(aList))   #set() 函数创建一个无序不重复元素集，但是这样会改变原来列表的元素顺序。
# print(bList)
# cList = {}.fromkeys(aList).keys()  #这个方法是利用了字典的 不重复性，把元素 先存放在一个字典中，然后再用 keys() 函数列出值。
# print(cList)

#使用这种方法也不会改变 原来元素的顺序。
# l1 = ['b','c','d','b','c','a','a']
# l2 = sorted(set(l1),key=l1.index)
# print(l2)

#使用循环
# aList = [1, 1, 3, 6, 9, 7, 3, 4, 4, 4, 6]
# bList = []
# for one in aList:
#     if one not in bList: #这个判断会把重复数据给过滤掉
#         bList.append(one)
# print (bList)

'''
请写一个函数reverse，参数是一个列表，该函数将列表中的所有元素倒序排列并返回
比如
reverse([1, 2, 3, 4]) ➞ [4, 3, 2, 1]
reverse([9, 9, 2, 3, 4]) ➞ [4, 3, 2, 9, 9]
reverse([]) ➞ []
'''
# alist = [1,2,3,6,5]
# alist.reverse()     #题目要求是倒叙排列 ，而不是降序排序 。 方法一：使用reverse() 函数
# print (alist)
#方法二：使用切片法
# print (alist[::-1])   #打印结果为 [5, 6, 3, 2, 1]

# def reverse(alist):
#     alist.reverse()
#     return alist
# reverse(alist)
# print (alist)
#只要是切片操作，获取到的数据类型都与 被 切片的数据类型一致。   序列类型都会存在越界

''' 课程内容：面向对象    6-5日布置
要求大家用面向对象的设计编写一个python程序，实现一个文字游戏系统。
动物园里面有10个房间，房间号从1 到 10。
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。
如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 
游戏3分钟结束后，显示每个房间的动物和它们的体重。
'''

'''
import time
from random import randint
#创建老虎类
class Tiger():
    className = '老虎'
    #实例属性
    def __init__(self,inWeight = 200):
        self.weight = inWeight
    #实例方法
    def roar(self):
        print ('Wow !!')
        self.weight -=5
    #实例方法
    def eat(self,food):
        if food == 'meat':
            self.weight +=10
            print ('喂食正确，体重增加10斤。')
        else:
            self.weight -=10
            print('喂食错误，体重减少10斤。')
#创建羊 类
class Sheep():
    className = '羊'
    def __init__(self,inWeight = 100):
        self.weight = inWeight
    def roar(self):
        print('mie~~')
        self.weight -=5
    def eat(self,food):
        if food == 'grass':  #可以使用异常来处理，如果输入不是meat 或者 grass时，程序可以提示继续输入正确的值。
            self.weight +=10
            print('喂食正确，体重增加10斤。')
        else:
            self.weight -=10
            print('喂食错误，体重减少10斤。')
#创建房间类
class Room():
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal
#初始化房间
roomList = []
for num in range(1,11):  #房间号是 1 到 10
    if randint(0,1) == 1:   #Return random integer in range [a, b], including both end points.
        animal = Tiger(200)
    else:
        animal = Sheep(100)
    room = Room(num,animal)
    roomList.append(room)
beginTime = time.time()
times = []  #想要知道玩家玩了几次，可以把输入的食物append到一个列表里，最后查看列表的长度，即为游戏的次数。
while True: #这个循环里面的代码有问题，最后输出的结果不正确，原因是548行（room.animal.roar()的代码应该是roomnum.animal.roar() ,roonnum 才是从房间中获取到的对象）和552行代码room.animal.eat(food)是一样的原因
    currTime = time.time()
    if currTime - beginTime > 20:
        print(f'********** 游戏时间到，游戏结束，您一共玩了{len(times)}次，欢迎下次光临！再见！ **********')
        for room in roomList:
            print (f'房间{room.num}中的动物是：{room.animal.className},现在的体重是：{room.animal.weight}斤。')
        break
    roomno = randint(1,10)  # randint()函数左右都包含，随机选择一个房间
    roomnum = roomList[roomno-1]  #因为房间号是 1-10,而需要从第一个房间开始，所以要减1
    knock = input(f'这里是{roomno}号房间, 请问需要敲门吗?[y/n]>>>')  #这里房间号不能用room.num ，因为需要每次房间是随机的。
    if knock == 'y':
        #room.animal.roar()  #代码改变的一直是房间10 ，是因为 房间初始化 for循环结束时，room是房间10 导致的。
        roomnum.animal.roar()
    food = input('请投喂食物(请选择meat或者grass)>>>').strip()
    if food == 'meat' or food == 'grass':
        #room.animal.eat(food)  #代码改变的一直是房间10 ，是因为 房间初始化 for循环结束时，room是房间10 导致的。 已经与心田老师确认了。
        roomnum.animal.eat(food) #
        times.append(food)
'''



#这个代码现在有个漏洞，如果时间到了（一直不输入），游戏本应该结束，但是目前不会结束。  --需要使用多线程来实现。

# while True:
#     curTime = time.time()
#     if (curTime - beginTime) > 5:
#         print('**********  抱歉，游戏时间到，游戏结束，欢迎下次光临！再见！ **********')
#         for room in roomList:
#             print (f'房间{room.num}中的动物是：{room.animal.className},现在的体重是：{room.animal.weight}斤。')
#         break
#     roomno = randint(1,10) #随机选择一个房间
#     room = roomList[roomno-1]  #因为房间号是 1-10,而需要从第一个房间开始，而roomList列表的下标是从0开始，所以要减1
#     knock = input(f'这里是{roomno}号房间, 请问需要敲门吗?[y/n]>>>')
#     if knock == 'y':  #如果敲门，则调用roar()函数，减去5斤。
#         room.animal.roar()
#     food = input('请投喂食物(请选择meat或者grass)>>>').strip()
#     if food == 'meat' or food == 'grass':
#         room.animal.eat(food)


'''
class Tiger():
    def roar(self):
        print('父类-Tiger-的实例方法')
    @staticmethod   #装饰器
    def tell():
        print('父类Tiger-的静态方法')
# t1 = Tiger()
# t1.tell()

class Sheep():
    def roar(self):  #实例方法
        print('父类-Sheep-的实例方法')
    @staticmethod  #装饰器
    def tell():
        print('父类-Sheep-的静态方法')

class SouTiger(Tiger,Sheep):  #继承了 Tiger() 和 Sheep() 类。
    def roar(self):
        print('子类的实例方法')

    @staticmethod
    def tell():
        print('子类的静态方法')

s1 = SouTiger()#创建子类的实例
#1- 直接使用，就直接调用子类自己的方法
# s1.roar()
#调用父类的实例方法---第一个父类优先
# super(SouTiger,s1).roar()
#调用父类的静态方法---第一个父类优先
super(SouTiger,s1).tell()

# super(Tiger,s1).tell()

#那么我们要调用第2个父类的方法---super(你要调用的那个父类的前一个父类-类名,s1).roar()
#1- 调用第2个父类的实例方法
# super(Tiger,s1).roar()
#2-调用第2个父类的静态方法
# super(Tiger,s1).tell()
'''

'''
#商城案例，需求：用户基数比较大，很多老VIP，需要一个更高的权限-SVIP：所有的VIP用户权限它都有。现在有一个VIP用户和一个SVIP用户，购买同一件东西后，查看各自的账户余额分别是多少。
# VIP用户--类
# 权限：折扣8折、生日券、礼品券
# 购买行为：全国包邮
# 用户登录系统的时候，通过 用户名 来判断是VIP 用户还是SVIP用户
class VIP(): #创建一个VIP用户类
    welfare = ['折扣8折','生日券','礼品券']
    #实例属性
    def __init__(self,inUsername):
        self.userName = inUsername
    #创建一个购买物品实例
    def shopping(self):
        print (f'VIP用户享有的福利有{self.welfare[0]}、{self.welfare[1]}、{self.welfare[2]}。')

    #创建一个物品实例
    def Goods(self,inPrice):
        self.price = inPrice

    #创建一个账户实例
    def Acount(self,inAcount,inPrice):
        self.acount = inAcount
        self.acount -= inPrice
        return self.acount

# SVIP用户--类    入会费  ：600
# 权限：折扣8折、生日券、礼品券、 金额、理财服务
# 购买行为：全国包邮   +  礼品---一年有3次机会
class SVIP(VIP):  #创建一个SVIP类，并集成 VIP类
    svipWelfare = ['折扣8折','生日券','礼品券','金额','理财服务']
    #创建实例属性
    def __init__(self,inUsername,inLevel):
        VIP.__init__(self,inUsername)
        self.level = inLevel
    def shopping(self):
        print(f'SVIP用户享有的福利有{self.svipWelfare[0]}、{self.svipWelfare[1]}、{self.svipWelfare[2]}、{self.svipWelfare[3]}、{self.svipWelfare[4]}。')

#创建一个商品类
class Goods():
    def __init__(self,inPrice):
        self.price = inPrice

#初始化 vip1 用户的账户，假设账户余额为1000块钱。
vip1 = VIP('vampire')
vip1.Acount(1000,500)

#初始化 svip1 用户的账户，假设账户余额也是1000块钱。
svip1 = SVIP('zhangsan','Level3')
svip1.Acount(1000,500)

#假设VIP用户 和 SVIP用户购买同一个东西的价格为500块钱
g1 = Goods(500)
print (vip1.shopping().Acount(2000,500))
print (vip1.Acount(2000,500))
'''

# flag = True
# while flag:
#     li = ["手机", "电脑", "鼠标垫", "游艇"]
#     for i in li:
#         print('{}\t\t{}'.format(li.index(i)+1,i))
#     num_of_chioce = input('请输入选择的商品序号/输入Q或者q退出程序：')
#     if num_of_chioce.isdigit():
#         num_of_chioce = int(num_of_chioce)
#         if num_of_chioce > 0 and num_of_chioce <= len(li):
#             print(li[num_of_chioce-1])
#         else:print('请输入有效数字')
#     elif num_of_chioce.upper() == 'Q':break
#     else:print('请输入数字')



# class FooBar:
#     def __init__(self):
#         self.somevar = 42
#     def A(self,inSum):
#         self.sum = inSum
#         print (inSum)
#
# f = FooBar()
# print (FooBar.A(self=3))


# username = "yangxiaoer"
# password = "123456"
# i = 3
# while i > 0:
#     zh = input("请输入你的账号:")
#     i -= 1
#     if zh == username:
#         mm = input("请输入你的密码:")
#         if mm == password:
#             print("验证成功.正在登陆......")
#             print('''恭喜你登陆成功!
#             欢迎用户进入
#             用户名 :%s
#             密码   :%s
#             '''%(zh,mm))
#             break
#         else:
#             print("密码错误,请重新输入")
#             print("你还有"+str(i)+"次机会")
#     else:
#         print("请输入正确的用户名!")
#         print("你还有" + str(i) + "次机会")


# 现已实现以下功能 my_log、my_name、my_shopping_mall 函数
# 要求编写装饰器，为 my_log、my_name、my_shopping_mall 函数加上认证的功能，要求登录成功一次，后续的函数都无需再输入用户名和密码
# 账户名密码来自字典变量
# 补充知识: token
# token的意思是“令牌”，是服务端生成的一串字符串（这里我们可以随意指定一个字符串），作为客户端进行请求的一个标识。
#当用户第一次登录后，服务器生成一个 token 并将此 token返回给客户端，以后客户端只需带上这个 token 来请求数据即可，无需再次带上用户名和密码
'''
from random import randint

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
'''

#在函数内部 也可以定义 类。
# def foo():
#     class Test():
#         print ('this is Test class')
#         def inner(self):
#             print ('this is inner')
#
# foo()

'''
#使用多线程实现，当时间到达120s时，游戏结束。需要用到，守护线程。
import time,threading,os
from random import randint
#创建老虎类
class Tiger():
    className = '老虎'
    #实例属性
    def __init__(self,inWeight = 200):
        self.weight = inWeight
    #实例方法
    def roar(self):
        print ('Wow !!')
        self.weight -=5
    #实例方法
    def eat(self,food):
        if food == 'meat':
            self.weight +=10
            print ('喂食正确，体重增加10斤。')
        else:
            self.weight -=10
            print('喂食错误，体重减少10斤。')
#创建羊 类
class Sheep():
    className = '羊'
    def __init__(self,inWeight = 100):
        self.weight = inWeight
    def roar(self):
        print('mie~~')
        self.weight -=5
    def eat(self,food):
        if food == 'grass':  #可以使用异常来处理，如果输入不是meat 或者 grass时，程序可以提示继续输入正确的值。
            self.weight +=10
            print('喂食正确，体重增加10斤。')
        else:
            self.weight -=10
            print('喂食错误，体重减少10斤。')
#创建房间类
class Room():
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal
#初始化房间
roomList = []
for num in range(1,11):  #房间号是 1 到 10
    if randint(0,1) == 1:   #Return random integer in range [a, b], including both end points.
        animal = Tiger(200)
    else:
        animal = Sheep(100)
    room = Room(num,animal)
    roomList.append(room)

# 定义一个函数，计算开始时间和游戏结果时间
def totalTime():
    beginTime = time.time()
    while True:
        currentTime = time.time()
        total_time = currentTime - beginTime
        if total_time > 10:
            break
    # print(f'********** 游戏时间到，游戏结束，您一共玩了{len(game())}次，欢迎下次光临！再见！ **********')
    for room in roomList:
        print(f'\n房间{room.num}中的动物是：{room.animal.className},现在的体重是：{room.animal.weight}斤。')
    os._exit(0)

def game():
    times = []  #想要知道玩家玩了几次，可以把输入的食物append到一个列表里，最后查看列表的长度，即为游戏的次数。
    while True:
        roomno = randint(1,10)  # randint()函数左右都包含，随机选择一个房间
        roomnum = roomList[roomno-1]  #因为房间号是 1-10,而需要从第一个房间开始，所以要减1 。列表是从 0 开始取值。
        knock = input(f'这里是{roomno}号房间, 请问需要敲门吗?[y/n]>>>')  #这里房间号不能用room.num ，因为需要每次房间是随机的。
        if knock == 'y':
            #room.animal.roar()  #代码改变的一直是房间10 ，是因为 房间初始化 for循环结束时，room是房间10 导致的。
            roomnum.animal.roar()
        food = input('请投喂食物(请选择meat或者grass)>>>').strip()
        if food == 'meat' or food == 'grass':
            #room.animal.eat(food)  #代码改变的一直是房间10 ，是因为 房间初始化 for循环结束时，room是房间10 导致的。 已经与心田老师确认了。
            roomnum.animal.eat(food) #
            times.append(food)
#创建一个线程实例
t1 = threading.Thread(target=totalTime)
t1.setDaemon(True)   #设置一个守护线程，如果子线程没有运行结束，则主线程会一直等待
t1.start()  #启动线程
#创建一个游戏线程实例
g1 = threading.Thread(target=game)
g1.setDaemon(True)   #设置一个守护线程，如果子线程没有运行结束，则主线程会一直等待
g1.start()  #启动游戏线程

#这个是主线程 ??
print(f'********** 游戏时间到，游戏结束，欢迎下次光临！再见！ **********')

#为什么设置了守护线程，但是并没有生效？？？？？
'''


# 先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。
# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
# 然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容
# http://mirrors.163.com/centos/6/isos/x86_64/README.txt
# http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt
# 主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
#如下代码是我写的方法
'''
import requests,threading
def get_text_centos6():
    url_centos6 = 'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
    headers_centos6 ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    res_centos6 = requests.get(url_centos6,headers=headers_centos6)
    return (res_centos6.encoding, res_centos6.text)

def get_text_centos7():
    url_centos7 = 'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
    headers_centos7 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    res_centos7 = requests.get(url_centos7,headers=headers_centos7)
    return (res_centos7.encoding,res_centos7.text)

t_centos6 = threading.Thread(target=get_text_centos6)
t_centos6.start()
t_centos6.join()    #在这里这个阻塞根本没用，因为主线程的代码需要依赖 子线程，所以不需要阻塞主线程。

t_centos7 = threading.Thread(target=get_text_centos7)
t_centos7.start()
t_centos7.join()    #在这里这个阻塞根本没用，因为主线程的代码需要依赖 子线程，所以不需要阻塞主线程。

if get_text_centos7()[0] == get_text_centos6()[0]:
    file_encoding = get_text_centos7()[0]
    with open('readme89.TXT','w',encoding=file_encoding) as fo:
        fo.write(f'The following content is from http://mirrors.163.com/centos/6/isos/x86_64/README.txt \n {get_text_centos6()[1]}\n')
        fo.write(f'The following content is from http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt \n {get_text_centos7()[1]}')
elif get_text_centos7()[0] != get_text_centos6()[0]:
    bytes_centos7 = bytes(get_text_centos7()[1], encoding=get_text_centos7()[0])
    bytes_centos6 = bytes(get_text_centos6()[1], encoding=get_text_centos6()[0])
    with open('readme89.TXT','wb') as fo:
        fo.write(bytes_centos6)
        fo.write(bytes_centos7)
'''

'''
#如下代码是老师提供的方法
import requests
import threading
urls = [
'http://mirrors.163.com/centos/6/isos/x86_64/README.txt',
'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt',]
# 对应urls 依次存储网页文件内容, 先创建同样个数的元素占位
fileContentList = [None for one in urls]
# 锁对象，用来控制访问 fileContentList
lock = threading.Lock()
def thread_entry(idx,url):
    print('thread #%s start' % idx)
    r = requests.get(url)
    # 注意上面的代码不应该放在获取锁的代码中
    lock.acquire()
    # 注意 r.text的类型是unicode，可以在文档中查到
    fileContentList[idx] = r.text
    lock.release()
    print('thread #%s end' % idx)
if __name__ == '__main__':
    print('main thread start.')
    threadpool = []
    for idx,url in enumerate(urls):
        t = threading.Thread(target=thread_entry,args=(idx,url))
        t.start()
        threadpool.append(t)
    # 等所有 线程结束
    for t in threadpool:
        t.join()
    # 所有线程结束后，所有内容都获取到了，合并内容
    mergeTxt = '\n\n----------------------\n\n'.join(fileContentList)
    print(mergeTxt)
    with open('readme.txt','w',encoding='utf8') as f:
        f.write(mergeTxt)
    print('main thread end.')
'''

'''
# 2020-7-8日作业
# 访问：https://m.weibo.cn/
# 点击：大家都在搜
# 找到：微博热搜榜
# 点击：微博热搜榜
# 找到：实时热点，每分钟更新一次
# 将其中带有 热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://m.weibo.cn/')
driver.maximize_window()
# 点击：大家都在搜
sleep(1)
driver.find_element_by_css_selector('.m-font-search + div').click()
sleep(2)
# 找到：微博热搜榜 ,点击：微博热搜榜
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4').click()
sleep(2)
hotLists = driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div')
singleHot = hotLists.find_elements_by_class_name('card4')
for ele in singleHot:
    hotTitle = ele.find_element_by_class_name('main-text').text  #热搜榜的标题
    #图片元素
    imgele = ele.find_elements_by_class_name("m-link-icon")
    if imgele: #如果图片存在
        keyword = imgele[0].find_element_by_tag_name('img').get_attribute('src').split('_')[1].split('.')[0]
        if keyword == 'hot':
            hotType = '热'
            print (f'{hotType}：{hotTitle}')
        elif keyword =='new':
            hotType = '新'
            print(f'{hotType}：{hotTitle}')
        elif keyword =='recom':
            hotType = '荐'
            print(f'{hotType}：{hotTitle}')
        elif keyword =='fei':
            hotType = '沸'
            print(f'{hotType}：{hotTitle}')
sleep(6)
driver.quit()
'''


"""
#2020-7-10日布置的作业（webUI获取断言信息 + 设置元素等待）
# 题目要求：http://vip.ytesting.com/q.do?a&id=ff80808171274e2d01712fd65eff0634
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://www.vmall.com/')
driver.maximize_window()
def print_level1_products(ele):
    '''
    :param ele: 一级菜单“手机”、“笔记本”等元素，而不是他们的父元素.
    :return: 不需要返回值
    '''
    #找到手机所在的 父标签元素，并点击。    如果是手机这个元素的话，点击了以后会跳转到新的界面。
    # driver.find_element_by_xpath('//*[@id="zxnav_0"]/div[1]/div').click()
    Level1_Ele = driver.find_element_by_xpath(ele)
    #实例化一个鼠标actions
    actions = ActionChains(driver)
    #鼠标移动到手机这个元素上
    actions.move_to_element(Level1_Ele).perform()
    #获取到 一级菜单下的 所有的 产品
    Level1_Eles = driver.find_elements_by_xpath('//*[@class="subcate-item"]/a/p/span')
    print (f'一级菜单：{Level1_Ele.text}')
    for pro in Level1_Eles:
        if pro.text != '':
            print (f'    {pro.text}')

#手机元素
phoneEle = '//span[contains(text(),"手机")]'
print_level1_products(phoneEle)
#笔记本元素
computerEle = '//span[contains(text(),"笔记本")]'
print_level1_products(computerEle)
#平板元素
minicomputerEle = '//li[@id="zxnav_2"]//span[contains(text(),"平板")]'
print_level1_products(minicomputerEle)
#智能穿戴&VR 元素
VREle = '//li[@id="zxnav_3"]//span[contains(text(),"智能穿戴&VR")]'
print_level1_products(VREle)
#智能家居
homeEle = '//li[@id="zxnav_4"]//span[contains(text(),"智能家居")]'
print_level1_products(homeEle)
#智慧屏 元素
wisdomEle = '//div[@class="category-item-bg"]//span[contains(text(),"智慧屏")]'
print_level1_products(wisdomEle)
#耳机音箱 元素
EarphoneEle = '//div[@class="category-item-bg"]//span[contains(text(),"耳机音箱")]'
print_level1_products(EarphoneEle)
#配件 元素
accEle = '//div[@class="category-item-bg"]//span[contains(text(),"配件")]'
print_level1_products(accEle)
#生态产品 元素
zoologyEle = '//div[@class="category-item-bg"]//span[contains(text(),"生态产品")]'
print_level1_products(zoologyEle)
#增值服务&其他 元素
value_added_Ele = '//div[@class="category-item-bg"]//span[contains(text(),"增值服务&其他")]'
print_level1_products(value_added_Ele)

def get_Hot():
    Hot = driver.find_element_by_xpath('//div[@class="span-968 fl"]/ul[@class="grid-list clearfix"]')
    actions = ActionChains(driver)
    # 鼠标移动到手机这个元素上
    actions.move_to_element(Hot).perform()
    # 获取热销单品
    HotSales = driver.find_elements_by_xpath('//div[@class="span-968 fl"]//a[@class="thumb"]')
    # print (HotSales)
    info = {}
    for Hotsale in HotSales:
        #因为某些手机没有“爆款”字样的图片，所以需要使用find_elements 找，找出来的是一个空列表，为假，如果爆款存在，为真，not(假 and 真) 为真，所以,continue,相当于舍弃了该种情况。
        if not (Hotsale.find_elements_by_xpath('./p[@class="grid-tips"]//span') and '爆款' in Hotsale.find_element_by_xpath('./p[@class="grid-tips"]//span').text):
            continue
        productName = Hotsale.find_element_by_xpath('./div').text.replace(u'\xa5', u'') #这里如果不加 replace(u'\xa5', u'') 会提示编码格式有问题。
        price = Hotsale.find_element_by_xpath('./p[@class="grid-price"]').text.replace(u'\xa5', u'')
        info['爆款'] = productName
        info['价格'] = price
        # print (f'爆款：{productName},价格：{price}')
    return info
print ('*'*20,'分隔符','*'*20)
if get_Hot():
    print (get_Hot())
else:
    print ('热销单品中没有爆款！')
driver.quit()
"""


'''
# 2020-07-12日布置 （控制浏览器操作 + webdriver 常用操作）
# 题目要求见 http://vip.ytesting.com/q.do?a&id=ff8080817238543f01723b6246cc011e
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('http://www.51job.com')
driver.maximize_window()
driver.implicitly_wait(0.5)
#点击高级搜索
driver.find_element_by_css_selector('a.more').click()
#输入搜索关键词 python
driver.find_element_by_id('kwdselectid').send_keys('python')
#地区选择 杭州
driver.find_element_by_id('work_position_input').click()
#删除默认 城市名 陕西省
sleep(1)
driver.find_element_by_id('work_position_click_multiple_selected_each_200000').click()
#然后点击 H I 那一行
driver.find_element_by_id('work_position_click_center_left_each_220200').click()
#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_220200_080200').click()
# 点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click()
#在选择职能类别之前需要先在其他地方点击一下， 防止搜索框搜索出来的内容遮挡住 职能类别 的选择框
driver.find_element_by_css_selector('div.d_lt.Fm > div:nth-child(3) > label').click()
#职能类别 选 计算机软件 -> 高级软件工程师
driver.find_element_by_id('funtype_click').click()
#点击 后端开发
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
# 选择 高级软件工程师
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
#公司性质选 外资 欧美
driver.find_element_by_css_selector('#cottype_list span.ic.i_arrow').click()
driver.find_element_by_css_selector('#cottype_list > div.ul > span:nth-child(3)').click()
#工作年限选 1-3 年
driver.find_element_by_css_selector('#workyear_list > span.ic.i_arrow').click()
driver.find_element_by_css_selector('#workyear_list > div.ul > span:nth-child(3)').click()
#点击 搜索按钮
driver.find_element_by_css_selector('div.btnbox.p_sou > span.p_but').click()
# 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
#     Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
#     Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
#     on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
resultListEle = driver.find_elements_by_css_selector('#resultList div.el + .el')
if not resultListEle:
    print ('对不起，没有找到符合你条件的职位！')
else:
    for oneEle in resultListEle:
        Position = oneEle.find_elements_by_css_selector('p.t1 a')[0].get_attribute('title')
        # Position = oneEle.find_elements_by_css_selector('p.t1 a')[0].text
        company = oneEle.find_elements_by_css_selector('span.t2 > a')[0].get_attribute('title')
        address = oneEle.find_elements_by_css_selector('span.t3')[0].text
        salary = oneEle.find_elements_by_css_selector('span.t4')[0].text
        time = oneEle.find_elements_by_css_selector('span.t5')[0].text
        print (f'{Position}|{company}|{address}|{salary}|{time}')
driver.quit()
'''







