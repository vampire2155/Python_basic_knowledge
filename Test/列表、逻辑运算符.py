print ('Hello World!')
print (2**32)  #表示2的32次方
import math
x = 2
y = 32
print (math.pow(x,y))
# print ('hello \n'*5)

#字符串 是一种 sequence类型 （序列类型） 。序列类型的特点：1、有下标   2、切片（有时候也称 分片）
#正下标  从右往左   从0到 n-1
info = '451236789'
print (info[8]) #打印的结果为 9

#负下标    从右往左   从-1 到 -n
#比如要获取 info字符串中的 数字5   有两种写法，一个是使用正下标 ，一个是使用负下标
print (info[1:2])
print(info[-8:-7])

#切片：分割字符串   --获取某段字符串   特点：被切对象不发生变化
a = '5689'
print (a[:1])  #打印的结果为 5

#扩展：字符串反序
b = 'abcdef'
print (b[::2])  #打印的结果为  ace
print (b[::-1])  #打印的结果为  fedcba    -1表示步长，表示每隔 1 取一个字符。
print (b[::-2])  #打印的结果为  fdb

'''# -----------day4-------------
列表 也是一种  sequence 类型  ，特点：可以存储  任何类型的 数据，每个元素是  任意类型。
'''
aList = [12,'sdf',122,[222,666,355]]
#如果要获取aList 列表中的 最后一个 元素 （即列表）中的222 元素
print (aList[-1][0])
print (222 in aList)  #打印结果为 FALSE。 222 不在列表aList  中，因为aList 列表中的元素分别为  12  ‘sdf’ 122 以及列表 [222,666,355]
#列表常用的操作：1、查找元素   2、修改元素   3、增加元素     4、删除元素        5、合并列表

bList = [10,20,30,40]
#查询操作   即获取列表中的元素  ，比如要获取bList() 列表中的元素10
print (bList[0])
#修改操作   ---即修改列表中的某个元素， 比如要把bList() 列表中的元素10 修改为50
bList[0] = 50
print (bList)   #打印结果为 [50, 20, 30, 40] ，这时就把元素 10 修改为了 50
#比如要把bList() 列表中的元素10 和 20  修改为50和100
bList[0:2] = [50,100]  #打印结果为[50, 100, 30, 40]

#增加元素    ---有两种方法：
# 方法一、 列表名.append(需要增加的元素值)    增加在了列表的尾部 ，比如增加一个元素值 90
bList.append(90)
print (bList)   #打印结果为  [10, 20, 30, 40, 90]
#方法二、插入值   列表名.insert(需要插入的位置下标,插入的值)
bList.insert(1,22)
print (bList)  #打印的结果为 [10, 22, 20, 30, 40]
#如果要插入的位置下标 大于 该列表的最大下标 ，比如bList() 列表的最大下标 是 3 ，而插入的位置是 5或者5以上，则还是插入到4的位置
bList.insert(10,22)  #打印的结果为 [10, 20, 30, 40, 22]

#删除操作   有两种方法 --
# 方法一、使用下标删除  del bList[需要删除的元素的下标]
del bList[0]
print(bList)  #打印结果为 [20, 30, 40]   也可以使用切片的方式删除    比如 del bList[0:4]  则是把bList()列表的元素都删除掉  结果为[]
#方法二、使用 列表名.pop()  方法来删除，这种删除方法与  del bList() 删除的不同是，列表名.pop()方法删除后 有返回值，即会把删除掉的元素返回 回来
print(bList.pop(0))  #这个的打印结果是 10 ，即把删除掉的元素 10 返回来了。
print (bList)
#方法三： 列表名.remove(需要删除的元素的值)   remove()方法是三种删除方法中效率最差的一种，因为需要遍历 所有元素的值，然后再删除
bList.remove(20) #打印结果为 [10, 30, 40]
#怎么删除 列表中的重复元素的值
cList = [10,20,30,20,40,20,50,20]
#方法一：使用for循环
i = 20
for i in cList:
    if 20 in cList:
        cList.remove(20)
print (cList)

#方法二：使用while 循环
while 20 in cList:
    cList.remove(20)
print (cList)

#方法三：使用pop()方法或者 del 方法来删除
#思路：获取所有元素值为 20 的下标，然后进行删除
cList = [10,20,30,20,40,20,50,20]
for i,j in enumerate(cList):   #使用enumerate函数 获取列表中元素的下标。
    if cList[i] == 20:
        del cList[i]
print (cList)

#方法四：使用 列表名.index() 来获取元素的下标   ----不知道要怎么实现？？？
dlist = [10,20,30,20,40,20,50,20]
print (dlist.index(20,0,len(dlist)))   #打印结果是 1  ，不是预期的结果


#列表合并
flist = [1,2,3]
print (flist+[5,6,])   #这种方法属于临时合并，不会改变原有列表flist的值
flist.extend([22,66])  #Extend list by appending elements from the iterable. 说明，这种方法合并列表，会把元素增加在列表的结尾处。
print (flist)



'''
课后思考题
假如有两个列表：
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
将两个列表合并要求第二个列表中的元素添加到第一个列表中的随机位置，但是 list2 中的元素不能在第一个列表中的开头，
也不能在第一个列表中的相邻位置，并且list2 中元素的顺序不变.
比如这样就不行：
list3 = ['a', 1, 2, 'b', 3, 4]
list4 = [1, 2, 3, 'a', 'b', 4]
list5 = [1, 'b', 2, 3, 'a', 4]
怎样做才能满足这样的要求呢？
思路：
1、[1,@, 2,@, 3,@, 4,@] list2中的元素只能出现在@的地方
2、然后将 list2中的元素插入相应位置并保持顺序不变。
‘’‘'''
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']

#字符串不能通过下标去改变元素值

#元组  也是序列类型  特点：1、下标   2、可以进行切片  但是元组不能改变： 1、 元组中的任意一个元素都不能改变   2、元组中的元素个数不能改变
tuple1 = (10,20,30,40)
print (type(tuple1))   #打印结果为  <class 'tuple'>      tuple--[计] 元组
print (tuple1[0:2])   #打印结果为 (10, 20) 切片后的类型也是元组。  切片不会改变元组的类型。

#元组转列表 ，列表转元组
glist = [0,2,3,6,5]
tuple2 = (23,66)
new_tuple = tuple(glist)  #把列表转换成元组
print (new_tuple)  #打印结果为 (0,2,3,6,5)
new_list = list(tuple2)  #把元组转换成列表
print (new_list)    #打印结果为 [23,66]


#布尔表达式
#关系运算符  >  <   ==   !=
#   ==   表示值是否相等        is 表示是否为同一个对象（即id是否相同）
print ('abc' > 'bc') #字符串的比较：对应位置字符的acsii 值的大小 比较  a  97  A 65
# in   在.....里面
a = 'abcde'
print ('ab' in a) #打印结果为 TRUE   字符串的使用：可以是字符串中的一个元素 ，  也可以是字符串中连续的一段元素，但不能是不连续的元素。
print ('ac' in a)  #打印结果为FALSE

#逻辑 且  ----and---    一假为假，全真为真
def func():
    print ('Hello Wolrd!')
func()

#逻辑  或   ---or---   一真为真，全假为假
def func1():
    print ('I am a engineer!')
print (2 < 4 or func1())
#逻辑  不   --not--
not True
not False

#逻辑运算符的优先级: not >  and > or
#关系运算符优先级  >  逻辑运算符优先级
print (not 3 > 2 or 3>2 and 5!=3 )

print (False or 1 or 4+2>1+3 and 0) #结果为 1 ，因为：非零即True ，所以结果为： True
#运算过程： 4+2>1+3 and 0 的结果为 0 ；  False or 1的结果为 1；  1 or 0 的结果为 1

# import math
# print  (math.ceil(4.45)) #向上取整，即不论小数的第一位是大于5还是小于5，结果都是 5   math.ceil()方法是向上取整。






