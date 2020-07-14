#!/usr/local/bin/python
#encoding=utf-8
file_obj = open('a.txt', 'w')
b = file_obj.write("Hello World!!")
file_obj = open("a.txt", 'r')
c = file_obj.readline()

#下面代码中 b 是int 类型，而前面是String类型，这个时候应该怎么处理？？？   不能用加号连接，因为类型不一样
print ('a.txt文件中的内容的字符串长度为：',b)
print ('a.txt文件中的内容是：',c)


def micifang(x,y):
    print (x**y)

def fool(a,b):
    print (111111111111111)
    return a*3,b*4
result1 = fool(3,4)
print (result1)

