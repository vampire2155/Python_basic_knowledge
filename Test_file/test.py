# class DivideByZeroExcepiton(Exception):
#     error = 'Zero divisor'
#     print ('float division by zero')

# VIP 系统题库练习
# 题目一：请写一个函数reverse，参数是一个列表，该函数将列表中的所有元素倒序排列并返回
# 比如
# reverse([1, 2, 3, 4]) ➞ [4, 3, 2, 1]
# reverse([9, 9, 2, 3, 4]) ➞ [4, 3, 2, 9, 9]
# reverse([]) ➞ []
'''
def reverse(list):
    return list[::-1]
aList = [9, 9, 2, 3, 4,3,6,8,9,6,7,5]
print (id(aList))
print (reverse(aList))  #打印结果为 [5, 7, 6, 9, 8, 6, 3, 4, 3, 2, 9, 9]
print (id(aList))  #aList 列表没有变，因为id没有变
'''

# 题目二：请写一个函数tri_area，参数是三角形的底和高，请计算返回三角形面积，比如
# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50
'''
def tri_area(a,b):
    return int(a*b/2)  #除法，结果保留小数.根据题目的结果应该结果取整，所以使用了int()函数。
print (tri_area(3,2))
print (tri_area(7,4))
print (tri_area(10,10))
'''


# 题目三：请写一个函数remainder，参数是两个数字，请计算返回这两个数字相除的余数,比如
# remainder(1, 3) ➞ 1
# remainder(5, 5) ➞ 0
# remainder(7, 2) ➞ 1
'''
def remainder(a,b):
    return a%b   #  % 是取余数。
print (remainder(1, 3))
print (remainder(5, 5))
print (remainder(7, 2))
'''

# 题目四：请写一个函数concat，参数分别是两个列表，请返回两个列表合并的结果，比如
# concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]
# concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]
# concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
'''
def concat(aList,bList):
    aList.extend(bList)   #这种方法合并列表，会把元素增加在列表的结尾处。 extend()方法。
    return aList
aList = [1, 3, 5]
bList = [2, 6, 8]
print (concat(aList,bList))
'''


# 题目五：请写一个函数findLargestNum，参数分别是1个列表，里面的元素都是数字，请返回该列表中最大的数字，比如
# findLargestNum([4, 5, 1, 3]) ➞ 5
# findLargestNum([300, 200, 600, 150]) ➞ 600
# findLargestNum([1000, 1001, 857, 1]) ➞ 1001
'''
def findLargestNum(list):
    list.sort(reverse=False)  #或者使用Max()函数，直接找出最大值。
    return list[-1]
aList = [4, 5, 1, 3]
print (findLargestNum(aList))
print (findLargestNum([300, 200, 600, 150]))
print (findLargestNum([1000, 1001, 857, 1]))
'''


# 题目六：请写一个函数ctoa，参数是1个字母，请返回该字母对应的ASCII码数字，比如
# ctoa("A") ➞ 65
# ctoa("m") ➞ 109
# ctoa("[") ➞ 91
# def ctoa(a):
#     return ord(a)  #odr() Return the Unicode code point for a one-character string
# print (ctoa("A"))


# 题目七：请写一个函数is_symmetrical，参数是1个数字，请返回该数字是否对称，比如
# is_symmetrical(7227) ➞ True
# is_symmetrical(12567) ➞ False
# is_symmetrical(12521) ➞ True
# is_symmetrical(44444444) ➞ True
'''
def is_symmetrical(num):
    # 先转换为字符串
    str1 = str(num)
    len1 = len(str1)
    # 如果长度是奇数,去掉中间的数字
    if len1%2 == 1:   #除法，取余数
        str1 = str1[:len1//2] + str1[len1//2+1:]
    part1 = str1[:len1//2]
    part2 = str1[len1//2:]
    return part1 == part2[::-1]
print(is_symmetrical(1))
'''


# 题目八：请写一个函数find_odd，参数是1个列表，请返回该列表中出现奇数次的元素，比如
# find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
# find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
# find_odd([10]) ➞ 10
'''
aList = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
bList = []
def find_odd(list):
    for one in list:
        times = list.count(one)  #使用count()函数计算列表中各个元素的个数。S.count(value) -> integer -- return number of occurrences（出现） of value
        if times%2 == 1:  #除法，取余数
            bList.append(one)
    return bList[0]  #题目要求返回的是一个数值，所示，取新列表中的第一个元素。
print (find_odd(aList))
'''

# 题目九：ATM机允许4或6位PIN码，PIN码只能包含4位数或6位数字。
# 请写一个参数为字符串的函数，如果PIN有效则返回True，如果不是则返回False。比如
# is_valid_PIN("1234") ➞ True
# is_valid_PIN("12345") ➞ False
# is_valid_PIN("a234") ➞ False
# is_valid_PIN("") ➞ False
'''
def is_valid_PIN(str):
    if str.isdigit():
        if len(str) == 4 or len(str) == 6:
            return True
        else:
            return False
    else:
        return False
print (is_valid_PIN("1234"))
print (is_valid_PIN("12345"))
print (is_valid_PIN("a234"))
print (is_valid_PIN("dd"))
print (is_valid_PIN("000000"))
'''

# 题目十：请写一个函数，该函数 参数为1个字符串，请分析并返回包含字符串中所有大写字母索引的有序列表。比如
# indexOfCaps("eDaBiT") ➞ [1, 3, 5]
# indexOfCaps("eQuINoX") ➞ [1, 3, 4, 6]
# indexOfCaps("determine") ➞ []
'''
indexList = []
def indexOfCaps(str):   #这个函数如果字符串有重复的大写字母时，会出问题，其他情况下正常。
    for one in str:
        if one.isupper():
            indexList.append(str.index(one))
    return indexList
print (indexOfCaps("ABFA"))
# print (indexOfCaps("SSSSSSSSS"))  #这种情况会出问题。
'''
#如下函数经测试，没有问题。
# def indexOfCaps(str):
#     indexList = []
#     idx = 0
#     for one in str:
#         if ord('A') <= ord(one) <= ord('Z'):  #字符串中的字母的ASCII值在 大写字母 A 与大写字母 Z 之间
#             indexList.append(idx)
#         idx += 1
#     return indexList
# print (indexOfCaps("SSSSSSSSS"))


# 题目十一：请写一个函数，该函数 参数为1个列表，删除所有重复的元素，并以与旧列表相同的顺序返回新列表（减去重复项）。比如
# removeDups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]
# removeDups([1, 0, 1, 0]) ➞ [1, 0]
# removeDups(['The', 'big', 'cat']) ➞ ['The', 'big', 'cat']
'''
bList = []
def removeDups(list):
    for one in list:
        if one not in bList:
            bList.append(one)
    return bList
print (removeDups(['The', 'big', 'cat','cat','cat','cat',1,1,2,2,3,6]))
'''


# 题目十二:请写一个函数，该函数 参数为数字列表，请算出另外一个列表，里面每个元素依次是参数列表里面元素的累计和。比如 参数为[1, 2, 3, 4]
# 结果计算方法为[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
# 返回结果就应该是[1, 3, 6, 10]
'''
#方法一：
aList = [1, 3, 3, 4 ,6]
sumList = []
def sumElement(numList):
    i = 0
    while i < len(numList):
        if i == 0:
            sumList.append(numList[i])
        elif i > 0:
            # 新列表中的元素值的计算：i=0 —> sumList[0]=numList[0] ; i=1 -> sumList[1]=numList[1] + sumList[0] 以此类推
            sumList.append(numList[i] + sumList[i-1])
        i +=1
    return sumList
print (sumElement(aList))  #打印结果为 [1, 4, 7, 11, 17]

#方法二：取列表的前 i 个数相加。
sumList = []
def sumElement(numList):
    i = 0
    while i < len(numList):
        sumList.append(sum(numList[:i+1]))  #取列表的前 i 个数相加。
        i +=1
    return sumList
print (sumElement([1, 4, 7]))
'''


# 题目十三：请写一个函数，该函数 参数为一个字符串，请验证该字符串是否是一个合法的电话号码，合法返回True，否则返回False
# 规则如下
#  该字符串必须全部都是数字。
#  该字符串长度为11位。
#  该字符必须以数字1开头。
# 比如
# validate_phone("13423445566") ➞ True
# validate_phone(".23rfs") ➞ False
'''
def validate_phone(str):
    if str.isdigit():
        if len(str) == 11:
            if str.startswith('1'):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print (validate_phone("13423445566"))
print (validate_phone(".23rfs"))
'''


# 题目十四：为了训练即将到来的马拉松，小明每周进行一次长跑。如果一周比上周跑的里程多，这周就是被称之为 进展周
# 写一个函数progress_weeks，该函数参数是每周长跑的里程列表，这个函数要返回共有几个进展周。比如
# progress_weeks([3, 4, 1, 2]) ➞ 2
# # 因为(3->4) 和 (1->2) 这两次是提高了
# progress_weeks([10, 11, 12, 9, 10]) ➞ 3
'''
def progress_weeks(mileList):
    timeList = []  #也可以定义一个count变量，如果后面的元素比前面的元素大，则自增 1
    i = 1
    while i < len(mileList):
        if mileList[i] > mileList[i-1]:
            timeList.append(1) #两两相邻元素进行比较，如果后面的元素比前面的元素大，则在列表中append 一个数值。最后计算新列表的长度
        i += 1
    return len(timeList)

print (progress_weeks([3,4,1,2]))
print (progress_weeks([10,11,12,9,10,11,12,12,13]))  #6次
'''

#对应VIP系统的第18题
# 题目十五：写一个函数concat，该函数参数是n个列表，这个函数要将这n个列表拼接起来并返回。 注意n个数是不确定的。比如
# concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
# concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
# concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
# concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
'''
#使用while 循环实现如下：
def concat(*args):  #考察的是可变数量参数
    i = 1
    while i < len(args):
        new_list = args[0]
        new_list.extend(args[i])
        i +=1
    return args[0]

#使用for循环实现如下：
def concat(*args):
    result = []
    for one in args:
        result.extend(one)
    return result

print (concat([1, 2, 3], [4, 5], [6, 7]))
print (concat([1], [2], [3], [4], [5], [6], [7]))
print (concat([1, 2], [3, 4]))
print (concat([4, 4, 4, 4, 4]))
'''


'''
str1 = 'agcadssadjkl'
print(str1.index('a',3))  #打印结果为 3 ，即为第二个 a 在字符串中的 下标
print(str1.index('a')) #打印结果为 0 ，即为第一个 a 在字符串中的 下标
print(str1.index('a',4))  #打印结果为 7 ，即为第三个 a 在字符串中的 下标

str1 = "Roobunoob example....wow!!!"
str2 = "oob"
print(str1.find(str2,3)) #打印结果为 6 ，即为第二个 字符串 "oob" 在 str1 字符串中的 首字母的下标
# find(self, sub, start=None, end=None) 函数，
# sub:被查找“字符串” ；start 表示查找的首字母位置（从0开始计数。默认：0） ； end：表示查找的末尾位置（默认-1）
# 返回值：如果查到：返回查找的第一个出现的位置。否则，返回-1。

# list.index(obj)
# 注释：
# obj —— 要查找的对象。
# 返回值：该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
str1 = "Roobunoob example....wow!!!"
str2 = "oob"
print(str1.index(str2))  #打印结果是 1 。
'''


# 题目十六：写一个函数replace，该函数参数是两个字符串，
# 第一个参数给出一个源，第二个参数是指定范围。
# 要求该函数将 第一个参数里面的字符串中 落在第二个参数指定范围内的字符串替换为 # 号 比如
# replace("abcdef", "c-e") ➞ "ab###f"
# replace("rattle", "r-z") ➞ "#a##le"
# replace("microscopic", "i-i") ➞ "m#croscop#c"
# replace("", "a-z") ➞ ""
'''
def replace(p1,p2):
    source = list(p1)
    r1,r2 = p2.split('-')
    new = []
    for c in source:
        if  r1<= c <= r2:
            new.append('#')
        else:
            new.append(c)
    return ''.join(new)
res = replace("abcdef", "c-e")
print (type(res))
'''


# def print_hello(name, sex):
#     sex_dict = {1: u'先生', 2: u'女士'}
#     # print (sex_dict.get(sex))
#     print (f'Hello {name} {sex_dict.get(sex)}, Welcome to python world!')
#
# print_hello('tanggu', 2)
# print_hello(1, name='zhangsan')   #错误的传参方式。


# str1 = 'abcdefgh'
# list1 = str(str1)
# print (type(list1))
# new_str = ''.join(list1)
# print (new_str)
# print (type(new_str))

# dict1 = {(1,):1,(2,):2,(3):3}  #所以连接的类型必须 是  字符串。
# print ('-'.join(dict1))  #TypeError: sequence item 0: expected str instance, tuple found



# 写一个函数alphabet_index，该函数参数是1个字符串，
# 要求该函数返回一个新字符串，里面是 参数字符串中每个字母依次对应的 数字。如果是非字母，则忽略它
# 字母"a"和"A" 都对应 1, "b"和"B"都对应2, "c"和"C"对应3， 依次类推,比如
# alphabet_index("Wow, does that work?")
# ➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"
# alphabet_index("The river stole the gods.")
# ➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"
# alphabet_index("We have a lot of rain in June.")
# ➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"

# 65-A	 97- a        90-Z	122-z
'''
def alphabet_index(para):
    new = []
    for one in para:
        if not one.isalpha():
            continue   #删除掉不是字母的元素。
        one = one.lower()  #因为大写字母和小写字母对应的是同一个数字，所以都转换成大写 或者 小写
        num = ord(one)-ord('a')+1   #计算字符串中的字母 的ASCII值相对于字母a 的ASCII值 位置。
        new.append(str(num))
    return ' '.join(new)
print(alphabet_index("Wow, does that work?"))
'''

# 写一个函数keys_and_values，该函数参数是1个字典，
# 要求该函数返回一个列表，里面包含了2个元素也是列表，分别是 字典里面的key 和对应的 value，比如
# keys_and_values({ "a": 1, "b": 2, "c": 3 })
# ➞ [["a", "b", "c"], [1, 2, 3]]
#
# keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })
# ➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
#
# keys_and_values({ "key1": True, "key2": False, "key3": True })
# ➞ [["key1", "key2", "key3"], [True, False, True]
'''
#方法一：使用for 循环实现
values = []
keys = []
def keys_and_values(dict):
    for one in dict:  #one 是dict 字典中的 key值，即 键。
        if one not in keys:
            keys.append(one)
            values.append(dict[one])
    return [keys,values]
print (keys_and_values({ "key1": True, "key2": False, "key3": True }))
print (keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" }))

#方法二：使用内置函数keys()和 values()实现
def keys_and_values(dict):
    keyList = list(dict.keys())
    valueList = list(dict.values())
    return [keyList,valueList]
print (keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" }))
'''

# 自己写一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''
aList = [1,2,3,4,5]
print('插入数据前的列表:',aList)
num = int(input('Input a num:'))
for one in range(0,len(aList)):
    if int(num) > aList[-1]:
        aList.insert(len(aList)+1,num)  #使用aList.append(num) 更简单
    elif num < aList[0]: #这一个判断也是必不可少的。
        aList.insert(0, num)
    elif num > aList[one] and num < aList[one+1]:
        aList.insert(one+1,num)
    elif num == aList[one]:
        aList.insert(one, num)
        break
print('插入数据后的列表:',aList)
'''

# python中生成随机整数、随机小数、0--1之间小数方法
# from random import *
# print (randint(0,100))   #生成区间内的整数
#
# from numpy import random
# print (random.randn(3))  #随机生成 3 个小数,结果是 array。
# random.randn(2,3)       #是从标准正态分布中返回2个样本值。每个样本是由 3个 小数组成的数列（array）。
#
# print ('随机0--1之间的小数:',random.random())  #随机生成 0--1之间的小数


# 请用两种方法实现如下要求：用户输入任意两个数字 相加，如5+6，求出两个数字的和。
# 方法一：
# content = input('Input two digit(eg:5+6):')
# a,b = int(content.split('+')[0].strip()),int(content.split('+')[1].strip())
# print (a+b)

# 方法二：
# content = input('Input two digit(eg:5+6):')
# index = content.find("+")
# a = int(content[0:index].strip())
# b = int(content[index+1:].strip())
# print (a+b)


# 任意输入一串文字+数字 统计出来数字的个数如'1234324324fdsaf1fdsaf12'
'''
# 方法一：
content = input('Input a content:')
aList = []
for one in content:
    if one.isdigit():
        aList.append(int(one))
print (f'输入的内容中数字的个数为{len(aList)}.')

# 方法二：
content = input('Input a content:')
count = 0
for one in content:
    if one.isdigit():
        count +=1
print (f'输入的内容中数字的个数为{count}.')
'''


# 开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["谁啊","牛逼",”无语”,”小朋友”]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
'''
li=["谁啊","牛逼","无语","小朋友"]
new_li= []
info = input("请输入评论内容:>>>")
for i in li:
    if i in info:
        len1 = len(i)
        info=info.replace(i,'*'*len1)   #   *len1  表示乘以i 的长度，  比如  ‘*’*5 --> *****
new_li.append(info)
print(new_li)
'''


# 输出商品列表，用户输入序号，显示用户选中的商品
# 商品 li = ["手机", "电脑", '鼠标垫', '游艇']
# 要求：1：页面显示 序号 + 商品名称，如：1 手机  2 电脑
#      2： 用户输入选择的商品序号，然后打印商品名称
#      3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#      4：用户输入Q或者q，退出程序。
'''
content = input('请输入商品的序号>>>')
li = ["手机", "电脑", '鼠标垫', '游艇']
flag = True
while flag:
    if content.isdigit():
        num = int(content)
        for i in range(1,len(li)+1):
            if num >=1 and num <=len(li) :
                print (num,li[num-1])
                flag = False
                break
            elif num < 1 or num > (len(li)):
                print('输入的商品序号有误，请重新输入！')
                content = input('请输入商品的序号>>>')
                num = int(content)
    elif content == 'Q' or content =='q':
        flag = False
    else:
        flag = False
'''

# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''
li= [11,22,33,44,55,66,77,88,99,90]
lessList = []
bigList = []
for one in li:
    if one > 66:
        bigList.append(one)
    else:
        lessList.append(one)
print ({'k1':bigList,'k2':lessList})
'''

# 写函数，计算传入字符串 '+0-0skahe817jashf wet1' 中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。
#如下代码实现有个问题是无法检测  中文字符
'''
content = input('Input a string>>>')
def countNum(str):
    numCnt, alpCnt, blankCnt, otherCnt = 0, 0, 0, 0
    for one in content:
        if one.isdigit():
            numCnt +=1
        elif one.isalpha():
            alpCnt +=1
        elif one == ' ':
            blankCnt += 1
        else:
            otherCnt +=1
    return f'输入的字符串中数字、字母、空格、其他的个数分别为:{numCnt}, {alpCnt}, {blankCnt}, {otherCnt}'
print (countNum(content))
'''


# 循环打印列表中每个元素，遇到列表则再循环打印出它里面的元素，li = [11,(1,2),4,"daben",[3,7,8,"Susan"],5,"xintian"]
# li = [11,(1,2),4,"daben",[3,7,8,"Susan"],5,"xintian"]
# for one in li:
#     if type(one) == list:
#         for i in one:
#             print (i)
#     else:
#         print (one)


# 查找li中的元素，并移除每个元素的空格，并找出以“S”或者“D”开头，并以“n”结尾的所有元素，
# 并添加到新列表，最后循环打出这个新列表。li =["Susan","Xintian","Xiaoxiao ","Xiaozhu","Daben","Xiaoze"]
'''
li =["Susan",'Ssusan  ',"Xiaoxiao ","Xiaozhu","Daben"," Xiaoze",'Ssusan',"Daben1"]
newList = []
for one in li:
    ele = one.strip()
    if (ele.startswith('S') or ele.startswith('D')) and ele.endswith('n'):
        newList.append(ele)
print (newList)
'''


# 判断下面的诗词是否是回文(把相同的词汇或句子，在下文中调换位置或颠倒过来，产生首尾回环的情况，叫做回文)。
# 苏轼的《菩萨蛮》题为《闲情》，其中一句： “迟日恨依依，依依恨日迟”
# str = "迟日恨依依，依依恨日迟"
# huiwen = str[::-1]
# if str == huiwen:
#     print ('是回文')
# else:
#     print ('不是回文')


# 写函数，接收n个数字，求这些参数数字的和。
# def sum(*args): # 可变数量参数
#     sum = 0
#     for one in args:  #args 是一个元组
#         sum +=int(one)
#     return sum
# print (sum(1,2,5,6,9))


# 问题:定义一个至少有两个方法的类:  getString:从控制台输入获取字符串    printString:打印大写母的字符串。
# class Multi():
#     def __init__(self):   #初始化方法
#         self.s = ''
#
#     def getString(self):
#         print('请输入字符串：')
#         self.s = input()
#
#     def printString(self):
#         print (self.s.upper())
# strObj = Multi()  #创建一个实例
# strObj.getString()  #实例调用  实例方法
# strObj.printString() #实例调用  实例方法


# 编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。
# 假设向程序提供以下输入:without,hello,bag,world
# 则输出为:bag,hello,without,world
# content = input('Input a string>>>')
# sortList = sorted(content.split(','),key=str.lower)
# print (','.join(sortList))
# li=[1,5,3,2]
# print ('before',id(list))
# print (sorted(li))
# print (id(sorted(li)))
# print ('after',id(list))

# li=[1,5,3,2]
# print ('before',id(li))
# print ('before',li)
# print (sorted(li))  #返回一个新的列表，对原列表没有任何影响
# print ('after',id(li))
# print ('after',li)


# 编写一个接受句子并计算字母和数字个数的程序。假设为程序提供了以下输入：
# Hello world! 123  然后，输出应该是：字母10 数字3
'''
content = input('Input a string>>>')
for one in content:
    alpCnt,numCnt = 0,0
    for one in content:
        if one.isalpha():
            alpCnt +=1
        elif one.isdigit():
            numCnt +=1
print (f'字母 {alpCnt}  数字 {numCnt}')
'''


# 编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示：
# D 100
# W 200
# D表示存款，而W表示提款。
# 假设为程序提供了以下输入：
# D 300
# D 300
# W 200
# D 100
# 然后，输出应该是：500
'''
netAcount = 0
while True:
    s = input('请输入事务日志（结束输入请按回车键）：')
    content = s.strip()
    if not s:  #怎么实现 判断出首字母是 W 或者 D 呢？？？？？
        print ('输入格式有误。')
        break
    values = content.split(' ')
    operation = values[0]
    acount = int(values[-1])
    if operation=="D":
        netAcount+=acount
    elif operation=="W":
        netAcount-=acount
    else:
        pass
print (f'银行帐户的净金额为：{netAcount}')
'''

# 输入某年某月某日，判断这一天是这一年的第几天？
# content = input('输入年月日(格式为：xxxx年xx月xx日)>>>')
# year = int(content.split('年')[0])
# month = int(content.split('年')[1].split('月')[0])
# day = int(content.split('年')[1].split('月')[1].split('日')[0])
# whichDay = month*30 + day
# print (f'{content}是{year}年的第{whichDay}天')


# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# content = input('请输入>>>')
# content.upper()
# fileDir = r'G:\Python_scripts\test.txt'
# with open(fileDir,'w') as fo:
#     fo.write(content.upper())


# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
I = int(input('Input profit(单位：元)>>>').strip())
if I <= 100000:
    prize = I * 0.1
elif I >100000 and I <=200000:
    prize = 100000 * 0.1 + (I-100000)*0.075
elif I >200000 and I <=400000:
    prize = 100000 * 0.1 + 100000 * 0.075 + (I-200000)*0.05
elif I >400000 and I <=600000:
    prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (I-400000)*0.03
elif I >600000 and I <=1000000:
    prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (I-600000)*0.015
elif I > 1000000:
    prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (I-1000000)*0.01
print (f'应发放奖金总数为：{int(prize)}元')
'''


# 打印出菱形图案
'''
for i in range(4):
    for j in range(3 - i):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print('')
#打印菱形的下半部分
for i in range(3):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(5 - 2 * i):
        print('*', end='')
    print('')
'''

# 用户登陆用户名为“yangxiaoer”密码为“123456”（三次输错机会）且每次输错误时显示剩余错误次数，错误次数为0时，结束程序
'''
username = 'yangxiaoer'
password = '123456'
def inputPWD():
    for i in range(3):
        pwd = input('请输入密码>>>')
        if pwd == password:
            print (f'密码输入正确. \n
                   ***{username}欢迎您***
                   ')
            return True
            break
        elif pwd != '123456':
            print (f'输入密码错误，您还有{2-i}次机会。')

for i in range(3):
    name = input('请输入用户名>>>')
    if name == username:
        if inputPWD() == True:
            break
    else:
        print (f'输入密码错误，您还有{2-i}次机会。')
#上面代码的优点是，如果用户名输入正确，密码输入错误时，不会再次要求输入用户名，而是直接再次输入密码，如果再次输入密码正确时，结束程序。
'''

# 猜年龄的游戏，年龄为48，猜错会有提示，直到猜对为止。
# age = 48
# inPutAge = int(input('请输入年龄>>>'))
# while True:
#     if inPutAge != age:
#         print ('年龄不正确，请重新输入.')
#         inPutAge = int(input('请输入年龄>>>'))
#     elif inPutAge == age:
#         print ('恭喜您，猜对了，再见！')
#         break


# 使用给定的整数n，编写一个程序生成一个包含(n, n*n)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# 假设向程序提供以下输入:8
# 则输出为:{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
# content = int(input('请输入>>>'))
# dict = {}
# for one in range(1,content+1):
#     if one not in dict:
#         dict.update({one:one*one})
# print (dict)


# 网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。以下是检查密码的标准：
# 1. [a-z]之间至少有1个字母
# 2. [0-9]之间至少有1个数字
# 1. [A-Z]之间至少有一个字母
# 3. [$＃@]中至少有1个字符
# 4.最短交易密码长度：6
# 5.交易密码的最大长度：12
# 您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。打印出符合条件的密码，每个密码用逗号分隔。
# 例：如果以下密码作为程序的输入： ABd1234@1,a F1#,2w3E*,2We3345
# 然后，程序的输出应该是：ABd1234@1
import re
value = []
print("请输入：")
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    # else:
    #     pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (f"符合条件的密码为：{','.join(value)}")














