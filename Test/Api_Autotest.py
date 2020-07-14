var1 = 'a'
var2 = var1
print (var1)
print (var2)
var1 = 'b'
print (var1)
print (var2)

'''
python中任何变量的赋值
1、都不会修改变量原来指向对象的值
2、而是将变量指向一个新的对象而已
3、如果原来的对象有其他变量指向它，也不会改变其他变量的指向
'''

str = '''Python is 


great'''
print (str)

#字符串的切片操作
#
myname = 'My name is Jack'
print (myname[11:15])  #切片从字符串的第11个字符（包含第11个字符）到15个字符（不包含第15个字符）
print (myname[11:])    #切片从字符串的第11个字符（包含第11个字符）开始到末尾

aList = [1222,'2222w',['abc',12345,'Hello World1']]    #列表是用方括号表示
cTuple = (1,2222,'ddddd','45ere')                      #元祖是用圆括号表示
dTuple = 2222,'ddddd','45ereee'                        #元祖也可以不适用括号表示
bList = aList[1:]
print ('bList的值为：')
print (bList)
print (aList[0])
print (aList[2])
print (aList[2][2])