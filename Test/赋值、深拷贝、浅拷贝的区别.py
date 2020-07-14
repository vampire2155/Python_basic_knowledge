'''Python 的赋值、深拷贝、浅拷贝的区别
赋值： 对象的引用
深拷贝：copy 模块的 deepcopy 方法。完全拷贝了父对象及其子对象。
浅拷贝：copy 模块的 copy 方法。拷贝父对象，不会拷贝对象的内部的子对象。 如果列表有三层，也只拷贝 最外层，不会拷贝 里面的。
'''
#1、赋值  对象的引用
alist = [100,20,30,4]
blist = alist
print (id(alist))  #打印结果为 34705344
print (id(blist))  #打印结果为 34705344
blist.append(300)  #对blist 列表增加元素后，alist列表的元素也会增加，所以，alist 和 blist 列表是同一个列表。
print (alist)  #打印的结果为 [100, 20, 30, 4, 300]
print (blist)  #打印的结果为 [100, 20, 30, 4, 300]
#说明，赋值 没有改变对象的 地址，所以是对象的引用。


#2、浅拷贝   --拷贝父对象，不会拷贝对象的内部的子对象    浅拷贝需要用到copy 模块
import copy   #导入copy模块
clist = [1,2,3,[22,33,55]]  #clist列表
dlist = copy.copy(clist)
print (clist) #打印的结果为：  [1, 2, 3, [22, 33, 55]]
print (dlist) #打印的结果为：  [1, 2, 3, [22, 33, 55]]
print (id(clist)) #打印的结果为 52573632
print (id(dlist)) #打印的结果为 54098368
#浅拷贝后，两个列表的值一样，但是他们的地址发生了变化，此时说明，列表clist 和 dlist是两个不同的列表
#此时，验证一下，clist 和 dlist中的  子列表是否 是同一个列表
print (id(clist[-1]))  #打印的结果为 52630592
print (id(dlist[-1]))  #打印的结果为 52630592
#经验证，发现 clist和 dlist中的子列表的 地址是一样的，说明：两个列表的子列表是一样的。

#3、深拷贝   ---copy 模块的 deepcopy 方法。完全拷贝了父对象及其子对象。
import copy
elist = [23,34,56,[11,22,33]]
flist = copy.deepcopy(elist)
print (elist) #打印的结果为[23, 34, 56, [11, 22, 33]]
print (flist) #打印的结果为[23, 34, 56, [11, 22, 33]]
print (id(elist))  #打印的结果为 54098176
print (id(flist)) #打印的结果为  52604992
#从两个列表的id可以看出，两个列表 不是同一个列表
print (id(elist[-1])) #打印的结果为 52606080
print (id(flist[-1])) #打印的结果为 52603072
#从两个列表的子列表的ID可以看出，两个列表的子列表 也不是同一个列表。
#应用场景：从某个获取一个数据， 在不改变原始数据的前提下，想复制出来去操作。  这时就需要用到 深拷贝。
#总结：对于只有一层的列表而言，三种 拷贝  都是一样的。对于多层列表，三者 的拷贝结果 就不同了。

import  copy
glist = [1,[12,3,[55,3,6,6]]]
hlist = copy.copy(glist)
print (id(glist[-1]))
print (id(glist[-1][-1]))
print (id(hlist[-1]))
print (id(hlist[-1][-1]))

