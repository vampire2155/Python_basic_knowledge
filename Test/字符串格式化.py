'''
def func1(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
if func1(10,1): #非零即真，所以这个也会执行。
    print ('Hello World!')
'''


#字符串格式化：往字符串里面传递参数，也就是表达一个字符串
#字符串格式化方法一：    --- %
name = 'tom'
age = 20
#用字符串格式化方法一把 上述的两个变量拼接成一个字符串
info = 'My name is %s,I am %d years old.' % (name,age)   #如果有多个变量，必须把他们 放在一个元组 里。
print (info)  #打印结果为  My name is tom,I am 20 years old.
#符号： %s--表示用str()函数进行字符串转换     %d--表示转换成有符号十进制数
# %f --表示转换成浮点数（小数部分自然截断）    %x --表示转换成无符号十六进制（x/X代表转换后的十六进制字符的大小写） 16进制 0-9，a-f

#%d--表示转换成有符号十进制数
print ('%5d' % 2) #  %5d   元素的长度为5个   %正数值d  右对齐，左补齐，不够用空格补齐
print ('%-5d' % 2) #  %-5d   元素的长度为5个   %负数值d  左对齐，右补齐，不够用空格补齐
print ('%05d' % 2) #   %05d   元素的长度为5个   右对齐，左边用0补齐    -->打印结果为：  00002
# %f --表示转换成浮点数（小数部分自然截断）
print ('%f' % 3.14159265354)  #默认保留6位小数， --会四舍五入      打印结果为 3.141593
print ('%.3f' % 3.14159265354)   #表示 保留3位小数 --会四舍五入    打印结果为： 3.142     需要注意3前面的那个小数点
print ('%2f' % 3.14159265354)  #这样的写法没有意思，打印的结果还是 3.141593
print ('%3.2f' % 3.14159265354)  #对于浮点型：如果长度要求（指的是字符串总的长度，即本例中的3） 小于 传入值本身长度（2），不理会该要求
print ('%5.2f' % 3.14159265354) #打印的结果为：  3.14  前面有两个空格。

#字符串格式化方法二： 字符串.format()        --格式化以后的类型还是字符串
#1)方法一：顺序填值   这种方法可以指定宽度. 顺序填值法，  数字型  默认向右对齐，str类型  默认向左对齐。
# {:方向 宽度}  -->{：> 5}  或者{:< 4 }   >表示向右对齐   <表示向左对齐   ^ 居中对齐    不够的默认用空格补齐。5  4  表示指定宽度
#{: * > 6} 表示右对齐，不够的用 * 号补齐。  *号可以放在6和 >的中间，但是，这样有时会出错，必须把 *号放在 ：（冒号）和 >中间。
#如果指定的宽度 小于 字符串本身的长度，则还是输出字符串的长度。例如； 'My name is {:> 1},I am {} years old.'.format(name,age)
name = 'Jack'
age = 21
Stu_info = 'My name is {},I am {} years old.'.format(name,age)  #
#Stu_info = 'My name is {},I am {} years old.'.format(name)  #不能这样写，因为有两个位置，但是只传了一个变量。报错信息如下：
#IndexError: Replacement index 1 out of range for positional args tuple

#Stu_info = 'My name is {},I am {} years old.'.format(name,age,100) #这样写是可以的，因为多余的值没有作用。
print (Stu_info)
#右对齐
Stu_info = 'My name is {:*>6},I am {:*>6} years old.'.format(name,age)
print (Stu_info)   #打印结果为： My name is **Jack,I am ****21 years old.
#左对齐
Stu_info = 'My name is {:*<6},I am {:*<6} years old.'.format(name,age)
print (Stu_info)  #打印结果为： My name is Jack**,I am 21**** years old.
#居中对齐
Stu_info = 'My name is {:*^6},I am {:*^6} years old.'.format(name,age)
print (Stu_info)  #打印结果为： My name is *Jack*,I am **21** years old.

#2)方法二：下标填值   这种方法是把format()函数中的参数作为一个元组，然后把元组的下标填写到前面的字符串中的 大括号中。
# 下标填值的优点：只要  大括号中 填写了元组中元素对应的下标即可，不需要像 顺序填值 那样 一一对应。
name = 'Jack'
age = 21
Stu_info = 'My name is {0},I am {1} years old.'.format(name,age)
print (Stu_info)
# #下面这样写也是可以的。
Stu_info = 'My name is {0},I am {0} years old.'.format(name,age)
#下面这样写也可以。但是如果元组中只有2个元素，下标却写了3或者3以上的值，那样就是有问题的。
Stu_info = 'My name is {0},I am {2} years old.'.format(name,age,30) #取了(name,age,30)元组中的第二个元素给了years前面的那个变量。
#下面为错误示例：报错为：  IndexError: Replacement index 5 out of range for positional args tuple
# Stu_info = 'My name is {0},I am {5} years old.'.format(name,age,30)
print (Stu_info)

#3)方法二：变量填值
stu_info = 'My name is {name},I am {age} years old.'.format(name='Tommy',age=15)
print (stu_info)

#字符串格式化常见用法：
# 用法一：指定宽度         ---格式化以后的类型还是字符串类型。
'{}'.format(2)  #打印结果为 '2'
'{:3}'.format(3)   #打印结果为: '  3'     --3的前面有2个空格。
'{:>5}'.format(33)  #打印结果为:'   33'    --33的前面有3个空格。
'{:<5}'.format('HH')   #打印结果为：'HH   '    --HH后面有3个空格。
'{:^5}'.format(23)    #打印结果为：' 23  '    --23的前面有一个空格，后面有两个空格。
'{:8}'.format(3.1415)  #打印结果为：'  3.1415'     --3.1415前面有2个空格
'{:->7}'.format('分割线')  #打印结果为：'----分割线'

#用法二：十六进制
'{:x}'.format(108)   #打印结果为：6c      作用就是把  十进制的 数字 108  转换成 十六进制  6c
'{:X}'.format(108)   #打印结果为：6C
'{:#x}'.format(108)  #打印结果是：0x6c     x前面的 # 号的作用，就是格式化后 前面 加上  0x前缀。 0x就表示 是 十六进制 数值。
# 开头0x的含义：  开头的“0”令解析器更易辨认数，而“x”则代表十六进制（就如“O”代表八进制）

#用法三：小数
'{:.2f}'.format(3.1415926)  #打印结果为3.14   表示保留2位小数
'{:6.2f}'.format(3.1415926)   #打印结果为：  3.14  3.14前面有两个空格。   表示总长度取6位，小数保留2位
#如下两种方法的场景是什么？ 需要搞清楚。 即字符串本身有 大括号
'''
咨询心田老师说明说没有场景，
就是字符串中如果有{}
怎么输出
就是在外面再加一层{} 
'''
'{:09.2f}{{}}'.format(1234.56789023)   #打印结果为：001234.57{}
'{:09.2f}{{1}}{{3}}'.format(1234.56789023)  #打印结果为：001234.57{1}{3}

#扩展   Python3.6版本以后 新增的  f-string 方法：
stu_info = F'My name is {name},I am {age} years old.'   #在字符串前面加上 字母 f （大小写都可以），就可以把字符串格式化。
print (stu_info)


'''
请实现一个程序，实现如下需求点：
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
# 代码实现如下：
info = input("Please input students' info:")
j = 0
i = len(info.split(';'))-1
while j <i:
    name = info.split(';')[j].split(',')[0].strip()
    age = info.split(';')[j].split(',')[1].strip()
    j += 1
    print ('{:<20}'.format(name) + ':' + '{:0>2}'.format(age))
'''