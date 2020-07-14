'''
循环
while 循环
for循环
'''
#使用while循环，计算从1到100的和。
'''
sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i = i + 1
print('1到100的和为:',sum)

#for循环  通过序列迭代和通过序列索引迭代的性能差异
#理论结果：通过序列迭代 要比 通过序列索引迭代 块。 经过验证通过序列索引迭代比 通过序列迭代性能好，难道是验证的方法有问题，待向专业人士确认。
import time
#下面的代码为通过序列迭代     ---经过验证，这个耗时是0.034002
nameList = ['Mike1','Mike2','Mike3','Mike4','Mike5','Mike6','Mike7','Mike8','Mike9',
            'Mike10','Mike11','Mike12','Mike13','Mike14','Mike15','Mike16','Mike17',
            'Mike18','Mike19','Mike20','Mike21','Mike22','Mike23','Mike24','Mike25',
            'Mike26','Mike27','Mike28','Mike29','Mike30','Mike31']
print (time.time())
for eachName in nameList:
    print (eachName,'Lee')
print (time.time())
#下面的代码为通过序列索引迭代   ---经过验证，这个耗时是0.003
print (time.time())
for nameIndex in range(len(nameList)):
    print (nameList[nameIndex],'Lee')
print (time.time())

#写一个while循环，输出整型为0-10（要确保是0-10，而不是0-9或1-10）  while循环是根据条件执行。
one = 0
while one < 10:
    one =one + 1
    print (one)
#使用range()内建函数，做上面同样的事。 需要使用for 循环，for循环的使用场景：1、遍历操作   2、需要制定循环次数
for a in range(11):
    print (a)

#判断一个数是正数、还是负数，还是0，开始使用固定的数值，然后修改你的代码支持用户输入数值在进行判断
input_num = input('Please input a number:')
if input_num[0] == '-':
    print('您输入的数字为负数')
    if input_num.__contains__('.') and input_num[0] != '-':
        print('您输入的数字为负数')
elif input_num[0] == '+':
    print('您输入的数字为正数')
    if input_num.__contains__('.') and input_num[0] != '+':
        print('您输入的数字为正数')
elif input_num.isalpha():
    print('您输入的不是数字')
# 当输入字母和数字的组合或者特殊字符时，因为前面都没有进入判断条件，
# 所以，执行到下面这判断条件时，是包含有字母和数字的组合或者特殊字符的字符串，所以没法转换为int类型。所以会报错。
#切记int()只能转化由纯数字组成的字符串
# 这个题的最好办法是使用正则表达式进行判断
elif int(input_num.split('.')[0]) >= 0:
    print ('您输入的数字为正数')
else:
    num = int(input_num)
    if num > 0:
        print ('您输入的数字为正数')
    elif num < 0:
        print('您输入的数字为负数')
    else:
        print('您输入的数字为零')
'''
'''
#从用户那里接受一个字符串输入，然后逐字符显示该字符串。先用while循环实现，然后再用for循环实现
str = input('Please input a string:')
#先使用while循环实现，代码如下
str_index = 0
while str_index < len(str):  #不能写等于，否则会超出范围
    print(str[str_index])  #需要先打印出来，然后再自增加 1  ，否则会把字符串的第一个元素给丢掉。
    str_index = str_index + 1
#使用for循环实现，代码如下
for one in str:
    print (one)
'''

'''
#循环和操作符。创建一个包含五个固定数值的列表或者元组，输出他们的和。然后修改代码为接受用户输入数值。分别使用while 和for循环实现。
alist = [1,2,3,4,5]  #列表和元组的实现是一样的。
#while代码实现如下
sum = 0
index = 0
while index < len(alist):
    sum = sum + alist[index]
    index = index + 1
print ('使用while循环实现的列表的和为：',sum)

#for代码实现如下
sum = 0
for index in alist:
    sum = sum + index
print ('使用for循环实现的列表的和为：',sum)


#接受用户输入求和实现如下
# 1、while 循环代码实现如下：
bList = input('Please input a list:')
bList_new = bList.split(',')
index = 0
sum = 0
while index < len(bList_new):
    a = bList_new[index] #这行代码必须放在循环里面才可以，否则，index的值一直为0
    b = int(a)
    sum =sum + b
    index = index + 1
print (sum)

# 2、for循环代码实现如下：
bList = input('Please input a list:')
bList_new = bList.split(',')
index = 0
sum = 0
for index in bList_new:
    sum = sum + int(index)
print ('---',sum)
'''


#接受用户输入，判断输入的值是否 是 1 和 100之间的数，如果用户输入的数满足这个条件，则显示成功并退出。
# 否则显示一个错误信息然后再次提示用户输入数值，直到满足这个条件为止。
'''
#实现方法一：使用while循环，但是这种方法有个缺陷，当输入的是非数字时，会跳出循环，无法满足题目要求。
num = input('Please input a number:')
if num.isdigit():
    new_num = int(num)
    while new_num >= 1 and new_num <= 100:
         break
    while new_num <1 or new_num> 100:  #当输入的值在这个范围时，
         num = input('Please input a number:')
         new_num = int(num) #如果这里不给  new_num  这个变量赋值的话，while循环条件中的 new_num就没办法再获取到值，会一直执行输入这个循环。
    print ('成功')   #这条语句 不能放在循环里面，否则每次执行完输入（除第一次外）语句后都会打印一次。
else:
    print('输入有误，请重新输入！')

#实现方法二： 这种方法完美的满足了题目的要求。
while True:
    print ('输入的值是1和100之间的数时，显示成功并退出。')
    print ('输入的值是除1和100之间之外的数时，提示错误信息然后再次提示用户输入数值。')
    num = input('Please input a number:')
    if num.isdigit():
        new_num = int(num)
        if new_num >= 1 and new_num <= 100:
            print ('Success')
            break
        elif new_num < 1 or new_num > 100:
            print ('输入的数值不在1-100之间，请重新输入。')
    else:
            print ('您输入的是非数字，请重新输入。')
'''

'''
#循环和操作符。创建一个包含五个固定数值的列表或者元组，输出他们的平均值。
# Python 2 因为除法 不会保留小数，所以需要使用float()函数实现结果是小数。
#python 3的除法会保留小数，所以不需要使用float()函数实现结果是小数。
aList = [1,2,35,6,88]
sum = 0
for one in aList:
    sum = sum + one
print (sum/len(aList))
'''

'''
#写一个带文本菜单的程序,菜单项如下
# (1)取a个数的和
# (2)取a个数的平均值
# (X)退出。
#由用户做一个选择, 然后执行相应的功能。当用户选择退出时程序结束。  这个题目的要求是只能输入 1  2  X（大写），输入其他的都会报错。
def Text(b):     #定义一个函数
    while True:
        a = str(b)
        print ('(1)取'+ a +'个数的和')
        print ('(2)取'+ a +'个数的平均值')
        print ('(X)退出')
        choose = input('Please input your choose:')
        if choose == '1':
            i = 0
            sum = 0
            while i < b:
                num = int(input('Please input number:'))
                sum = sum + num
                i =i + 1
            print ('这'+ a +'个数的和为',sum)
        elif choose == '2':
            j = 0
            sumj = 0
            while j < b:
                num_avg = int(input('Please input number:'))
                sumj = sumj + num_avg
                j+=1
            print ('这'+ a +'个数的平均值为',sumj/5)
        elif choose == 'X':
            br            print ('退出')
eak
        else:
            print ('输入有误，请重新输入。')
Text(6)  #函数调用
'''
'''
#定义一个函数，计算start和end之间的数的和。 step为步长。
def get_sum(start,end,step=1):
    sum = 0
    cnt = start
    while cnt <= end:
        sum = sum + cnt
        cnt += step
    return sum
print (get_sum(1,10,3)) #即使step赋了默认值 1 ，还是以输入的实参为准。
'''
print ("I'm {1} years old, my name is {0}".format('Mike',5))
var1 = 'a\nb'
print (len(var1))

















