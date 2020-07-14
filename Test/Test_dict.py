#字典    字典是Python语言中唯一的映射类型。 字典不允许 一键  多个值。如： dict = {"name":"Jack","name":'Tom'} 这样前面的键-值对会被后面的覆盖到。

#1、增加字典
'''
dict1 = {}  #创建一个空字典
dict = {"name":"Jack","age":20}  #创建一个字典
# print (type(dict))    #打印结果为：  <class 'dict'>
#使用fromkeys() 函数来创建字典   不过使用fromkeys()创建的字典中的所有元素 的值都相同。如果使用此函数创建字典时没有给出值，则默认为None
dict2 = {}.fromkeys(('x','y','z'),23)
print (dict2)   #打印结果为： {'x': 23, 'y': 23, 'z': 23}

#字典增加元素
dict3 = {}
dict3['name'] = 'Jack'  #此时，dict3 = {'name':'Jack'}


#使用fromkeys() 函数来创建字典，不给出值时，默认为None
dict3 = {}.fromkeys(('x','y','z'))
print (dict3)   #打印结果为： {'x': None, 'y': None, 'z': None}

dict30 = {}.fromkeys(('age'),20)    #dict30 = {'a':20,'g':20,'e':20}
#！！！！注意上下这两条语句的区别！！！！
dict31 = {}.fromkeys((['age']),20)    #dict31 = {'age': 20}
'''

#2、字典的查询
'''
dict3 = {}.fromkeys(('x','y','z'))
print (dict.keys())   #查询字典所有的键      打印结果为：dict_keys(['name', 'age'])
print (dict.values())   #查询字典所有的值      打印结果为：dict_values(['Jack', 20])
print (dict.items())    #查询字典所有的键值对       打印结果为：dict_items([('name', 'Jack'), ('age', 20)])
print (dict["name"])   #通过键 查询字典的值
print (dict5.get('name'))   #get()函数获取字典中 键 对应的值
'''
# fdict = dict((['x',1],['y',2]))  #需要在python 解释器中运行才可以。Pycharm中运行会拨错。
# print (fdict)

#3、字典值的修改
'''
dict4 = {}.fromkeys(('score','age','width'),23)       #结果为  {'score': 23, 'age': 23, 'width': 23}
dict4['age'] = 30    #结果为：  {'score': 23, 'age': 30, 'width': 23}
print (dict4)
'''

#4、字典的删除  方法有： del    pop()    clear()    。   没有序列的remove()方法。
'''
dict4 = {}.fromkeys(('score','age','width'),23)
del dict4['score']   #删除 键为'score' 的元素
print (dict4)   #打印结果为： {'age': 23, 'width': 23}
dict4.clear()    #删除字典中所有的元素
print (dict4)   #打印结果为： {}  -->空字典
dict4.pop('age')
print (dict4)
'''

#5、查看字典中的元素的个数
# dict5 = {}.fromkeys(('name','info','message'),'Hello')
# print (dict5)

#6、字典的合并   ---update()方法
'''
dict6 = {}.fromkeys(('name','name1'),'Jack')   #dict6 = {'name': 'Jack', 'name1': 'Jack'}
dict60 = {}.fromkeys(('age','age2'),20)        #dict60 = {'age': 20, 'age2': 20}
dict6.update(dict60)  #此方法是 将 字典dict60中的键-值对 添加到 字典 dict6 中。
print (dict6)   #此时 dict6 = {'name': 'Jack', 'name1': 'Jack', 'age': 20, 'age2': 20}
'''

#7、字典的常用操作   in    not in
# dict7 = {}.fromkeys(['name','name1'],'Mary')
# print ('name' in dict7)   #True
# print ('aa' in dict7)     #False

#8、字典的拷贝
'''
dict8 = dict(name = 'Tom',age = 20)  #使用dict() 函数创建 字典 -->  dict8 = {'name': 'Tom', 'age': 20}
dict80 = dict8.copy()   #dict80 = {'name': 'Tom', 'age': 20}
print (dict80)
'''

#创建一个字典，并把这个字典中的键按照字母顺序显示出来
# dict9 = {'name':'Jack','age':20,'info':'I am a student','base':'Hello'}
# aList = list(dict9)
# for one in aList:
#     i = 0
#     for i in range(len(aList)-1):
#         if one[i] > one[i+1]:
#             print ([one[i+1],one[i]])
# print (aList)


'''
def sum(start,end,step=1):
    sum = 0
    i = start
    while i<=end:
        sum +=i
        i+=step
    return sum
print (sum(1,10,2))
'''








