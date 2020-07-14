#文件路径的三种写法：
# file_object = open(r'G:\Python_scripts\Test\a.txt')  #写法一：使用 r  取消转义
# file_object = open('G:\\Python_scripts\\Test\\b.txt') #写法二：使用  \  进行转义
# fileDir = 'G:/Python_scripts/Test/b.txt'
# file_object = open(fileDir,'a') #写法三：使用 / 编写
# file_object.write('123\n456')
# res = file_object.read()   #刷新到缓存中
# print (res)
#重要：先写文件，再读取文件：需要写完以后把文件关闭，然后再进行读取，如果没有关闭就直接读取，是读取不到内容的。
'''
file_object.close()
file_object = open(fileDir)
# print (file_object.readline())  #读取一行内容
# print (file_object.readlines()) #读取多行内容  ，不过也会把 换行符  \n  打印出来
# print (file_object.read().splitlines())
#如果此行代码前面已经把文件中的内容都读取完毕，文件的指针 已经到了末尾，
# 所以，再执行这条代码print (file_object.read().splitlines())，打印结果为  空列表
#如何解决上述问题呢？ 此时可以用到  文件内 移动的方法  seek()。
print (file_object.readlines())
file_object.seek(0,0)
print (file_object.read().splitlines())
# splitlines([keepends])函数，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。默认是False
#print (file_object.read().splitlines(True))   #这样写就是包含换行符的。

seek() 方法用于移动文件读取指针到指定位置。
语法
seek() 方法语法如下：
fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。 
1 和 2 模式，需要打开文件的时候使用 'rb' 二进制模式打开，否则会报错。
eg：
file_object = open(fileDir,'rb')
file_object.seek(1,1)
file_object.seek(1,2)
'''

#如果要打印文件中的每一行内容，有如下两种方法：

# 方法一：这种方法是读完所有的行才开始向屏幕输出数据，当文件很大时，这种方法会比较占内存。
# import time
# fileDir = r'G:\Python_scripts\Test\NEWS.txt'
# file_object = open(fileDir,'rb')
# allLines = file_object.readlines()
# file_object.close()
# print (time.time())
# for eachLine in allLines:
#     print (eachLine)
# print (time.time())


# 方法二：这种方法是每次只读取和显示一行。 每次占用内存小
# import time
# fileDir = r'G:\Python_scripts\Test\NEWS.txt'
# file_object = open(fileDir,'rb')
# print (time.time())
# for eachLine in file_object:
#     print (eachLine)
# print (time.time())

#刷新了  再写会不会把原来的数据清除掉？  如果使用 w 模式，肯定会把文件内容删除掉然后写入，如果是 a 模式，则会在原来内容的基础上继续写入。
# fileDir = r'G:\Python_scripts\Test\NEWS.txt'
# fo = open(fileDir,'a',encoding='utf-8')
# fo.write('新增加的内容。')
# fo.flush()   #文件关闭以后不能进行刷新
# fo1 = open(fileDir,'w')
# fo1.write('abc*****')


#题目要求：文件访问。 提示输入数字N和文件F，然后显示文件F的 前N 行内容。
#要 实现此功能，需要导入一个 linecache 模块。
# import linecache
# fileName = 'G:\\Python_scripts\\Test\\NEWS.txt'
# digit = 2
# def readFile(digit,fileName):
#     return linecache.getline(digit,fileName)
# readFile(digit,fileName)

#题目要求：文件信息，提示输入一个文件夹，然后显示这个文本文件的总行数
fileDir = r'G:\Python_scripts\Test\c.txt'
fo = open(fileDir,'a')
fo.write('1231000.3333\n abdc\ndfdsd')
fo.close()
fo = open(fileDir)
res = fo.read()
print (res)

