#!/usr/local/bin/python
#encoding=utf-8


#文件操作的流程:
#1、打开文件：建立程序与文件的联系
#读方式
#写方式
#2、读写文件
#read   readline    readlines  
#write   writelines
#3、关闭文件
#示例：
#file_object=open(filename,mode)   ----打开文件， mode 表示用什么方式打开
#filename :
#	原字符串  r'c:\tmp\text.t'
#	转义字串  'c:\\tmp\\text.t'
#mode:
#	r       ---表示读取文件
#	w       ---表示写入文件
#	a       ---表示追加式写入文件，每次都是在上次的基础上写入
#	+       ---
#	b       ---


file_obj = open('a.txt', 'r')
a = file_obj.read()
print (a)
