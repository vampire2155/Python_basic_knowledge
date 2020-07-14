#!/usr/local/bin/python
# encoding=utf-8
file_obj = open('a.txt', 'r')

line1 = file_obj.readline()  # 读取一行
line1 = line1.rstrip()    #strip() 函数的作用是去掉
print(line1)

line2 = file_obj.readlines()  # 读取多行
#lines2 = line2.strip()   #readlines  has no attribute of 'strip()'
print(type(line2))

boys = ['Mike', 'Jhon', 'Tom']
girls = ['Lisa', 'Linda', 'Mary']
for girl in girls:
    for boy in boys:
        print(girl, '<->', boy)

beforetax = [15000, 12000, 13000]
aftertax = []
for one in beforetax:
    aftertax.append(int(one * 0.9)) # append()函数的用法：
print(aftertax)


aList = [3,5,7,2]
newList = []
# for i in range(0,len(aList)-1):
#     for j in range(0,len(aList)-1-i):
#         if aList[j] < aList[j+1]:
#             aList[j],aList[j+1] = aList[j+1],aList[j]
#             newList.append(aList[len(aList)-1:len(aList)])
# print (newList)
for i in aList:
    newList.append(min(aList))
    aList.remove(min(aList))
print (aList)
print (newList)




# bList = [2,5,3,0,9]
# bList.sort(reverse=True)  #降序排序    sort() 函数默认 是降序排序
# print (bList)
# bList.sort(reverse=False)  #升序排序
# print (bList)