#对象的方法
#1、字符串的方法
#1）字符串的  计数  方法
a = 'abcdefa'
result = a.count('a')  #计算字符串 a 中有几个 字字符串 a ，结果为  2
print (result)
#2） endswith 检查字符串是否以指定的字符串结尾   返回值 为 布尔类型
print ('12 233 h'.endswith('h'))

#startswith 检查字符串 是否 以制定的字符串开头   返回值 为 布尔类型
print ('12 233 h'.startswith('1'))

#find 返回指定的子字符串在字符串中出现的位置
#如果元素存在则返回第一个字符串出现的下标，这里的第一个字符串 指的是 要查找的元素的第一个字符串。
#find() 函数与 index()函数的区别：
# index() 函数是获取已存在的元素的下标，如果存在则返回元素的下标，如果不存在则报错
# find() 返回指定的子字符串在字符串中出现的位置。如果存在则返回  “第一个字符串”  出现的下标。如果不存在则返回  -1
b = 'abcdefghgh'
print (b.find('gh'))  #打印结果为 6
print (b.find('y'))  #打印结果为 -1 ， 因为没有找到，所以返回 -1
print (b.index('a')) #打印结果为0
print (b.index('y'))  #会报错： ValueError: substring not found

#str.join 将squencepe类型（列表类型）的参数的元素字符串合并（连接）到一个字符串，str作为分隔符。
a = ';'
print (a.join(['I','like','play','football']))  #打印结果为：  I;like;play;football

#split() 函数 ：将字符串分割为几个子字符串。参数为分隔符。返回结果存在一个 列表 中。
'abcedafgha'.split('a')   #打印结果为['', 'bced', 'fgh', '']  切点会被切掉，即 a 会被切掉。 切了三次，所以结果是四个字符串。

#lower()  将字符串里面如果有大写字母的全部转为小写字母，转换前后类型不变。
'China'.lower()  #打印结果为  'china'
print (type('China'.lower()))    #<class 'str'> 转换后还是字符串

#upper 将字符串里面如果有小写字母的全部转换为大写字母，转换后类型不变
'China'.upper()  #打印结果为  'CHINA'
print (type('China'.upper()))  #<class 'str'> 转换后还是字符串

#replace()  替换字符串里面指定的子字符串，默认全部替换，如果需要替换指定的数量，则需要在增加参数
b = 'jakdkjfraajjj'
print (b.replace('j','y'))  #打印结果为 yakdkyfraayyy   默认是全部替换了
print (b.replace('a','t',2)) #打印结果为 jtkdkjfrtajjj   只替换了 2个 a 为 t

#作业：写一个replace() 函数，替换指定位置的子字符串

#剔除掉下面字符串中所有的空格，必须使用 strip() 函数进行操作。三个都是空格
c = '   a   b   g   '
'''
我的思路:
1、使用strip() 函数，替换掉 左右两边的空格
2、使用replace（）函数替换掉
'''
d = c.strip()
e = d.replace(' ','')
print (e)




