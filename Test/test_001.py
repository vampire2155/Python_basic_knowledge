'''
需求：有一个列表[3,5,8,2]
1、创建一个空列表newList
2、先找出列表中最小的元素，然后append 在 newList 列表中
3、再次找出剩余所有元素中的最小值，然后append 在 newList 列表中
4、以此类推，直到所有的元素都在newList 列表中
'''
import os

'''
思路：
1、使用min() 函数找出列表中的最小元素，append 在 新列表中
2、然后删除掉列表中的最小元素，再在剩余元素中找出最小元素，append 在 新列表中
3、以此类推，直到所有的元素都在新列表中
'''
# aList = [3,5,8,2,100,56,3,0]
# newList = []
# for i in range(len(aList)):
#     newList.append(min(aList)) # 把列表中最小元素 append在新列表中
#     aList.remove(min(aList)) #删除列表中的最小元素
# print ('aList列表为',aList)
# print ('newList列表为',newList)

# workBook = xlrd.open_workbook(excelDir)
# workSheet = workBook.sheet_by_name('1-登录接口')
# res = workSheet.row_values(2)   #获取第二行所有的值
# cols = workSheet.col_values(2)  #获取第二列所有的值
# print (res)
# print (cols)

# dict = {'key':{}}
# res = json.dumps(dict)
# print (type(res))

# import pytest
# class Test():
#     def setup(self):
#         print("setup：每个用例开始前执行（调用方法前）")
#     def teardown(self):
#         print("teardown：每个用例结束后执行（调用方法后）")
#     def setup_class(self):
#         print("setup_class:所有用例执行之前（类级）")
#     def teardown_class(self):
#         print("teardown_class:所有用例执行之后（类级）")
#     def setup_method(self):
#         print("setup_method:每个用例开始前执行（方法级）")
#     def teardown_method(self):
#         print("teardown_method:每个用例结束后执行（方法级）")
#     def test_one(self):
#         print("正在执行---test_one")
#     def test_two(self):
#         print("正在执行---test_two")
#     def login_test(self):
#         print("正在执行---login_test")
#
# if __name__ == '__main__':
#     pytest.main(['-s','test_001.py'])

'''
#并行，并发，线程，进程
import threading,time
def foo(something):
    print (something)
    time.sleep(1)
#磁盘写入数据  和 CPU处理其他事情  是串行执行。
# startTime = time.time()
# foo('磁盘写入数据')
# foo('CPU处理其他事情')
# endTime = time.time()
#串行执行为什么总耗时 是 2.0001144409179688 。因为每次调用了 foo()函数以后，都会等待 1s 。所以总共等待了2s。

#下面用并行实现 并行执行    总耗时 0.003000020980834961
startTime = time.time()
#创建线程实例
t1 = threading.Thread(target=foo,args=['磁盘写入数据'])   #args 参数也可以用 元组（tuple）传参。既可以用列表也可以用元组传参。
t2 = threading.Thread(target=foo,args=['CPU处理其他事情'])

#启动线程
t1.start()
t2.start()
endTime = time.time()
print ('\n总耗时',endTime-startTime)
'''

# import threading,time
# def foo():
#     # time.sleep(2) #如果 子线程不等待 这1s的话，就是先打印子线程，在打印 主线程。 但是 不论何时都是先运行（记得是运行）然后再运行子线程。
#     print ('子线程')
#     time.sleep(10)  #因为主线程被阻塞住，所以会在 子线程 执行完 10s 以后才去继续执行主线程。
#
# t1 = threading.Thread(target=foo)
# t1.start()
# t1.join()  #在t1子线程结束运行之前，阻塞住主线程，不让主线程继续往下运行
# print ('主线程')

# import os
# os.system('ipconfig')
# print ('11111')
# os._exit(0)  #0 表示正常退出  ，1 - 127 表示非正常退出。  _exit()用于子线程  sys.exit() 用于在主线程中退出
#
# import threading
# r = threading.Lock()  #申明一把锁，同步锁
# r.acquire()  #锁上
# r.release()  #解锁
#
# r = threading.RLock()  #申明一把锁，递归锁
# r.acquire()  #上锁
# r.release()  #解锁


#funA 作为装饰器函数
# def funA(fn):
#     fn() # 执行传入的fn参数
#     def inner():
#         print ('1')
#     return inner
#       #@get_token   #这一个操作相当于 my_log = get_token(my_log)
# def funB():
#     print ('B')
# funB = funA(funB)   # @funA
# funB()

#
# def funA(fn):
#     def say(arc):
#         print("Python教程:",arc)
#     return say
# @funA   #这行代码相当于  funB = funA(funB)
# def funB(arc):
#     pass
#
# funB("http://c.biancheng.net/python")




# #闭包函数，其中 exponent 称为自由变量
# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of # 返回值是 exponent_of 函数
# square = nth_power(2) # 计算一个数的平方
# cube = nth_power(3) # 计算一个数的立方
#
# print(square(3))  # 计算 2 的平方
# print(cube(2)) # 计算 2 的立方

# import threading
# import time
# global_num = 0
# lock = threading.Lock()
# def test1():
#     global global_num
#     lock.acquire()
#     for i in range(1000000):
#         global_num += 1
#     lock.release()
#     print("test1", global_num)
#
#
# def test2():
#     global global_num
#     lock.acquire()
#     for i in range(1000000):
#         global_num += 1
#     lock.release()
#     print("test2", global_num)
#
# t1 = threading.Thread(target=test1)
# t2 = threading.Thread(target=test2)
#
# t1.start()
# t2.start()



# import threading,time
# global_num = 0
# lock =threading.Lock()
# def test1():
#     global global_num
#     # lock.acquire()
#     test1_num = global_num
#     for i in range(1000000):
#         test1_num += 1
#     global_num = test1_num
#     # lock.release()
#     print("test1", global_num)
#
# def test2():
#     global global_num
#     # lock.acquire()
#     test2_num = global_num
#     for i in range(1000000):
#         test2_num += 1
#     global_num = test2_num
#     # lock.release()
#     print("test2", global_num)
# t1 = threading.Thread(target=test1)
# t2 = threading.Thread(target=test2)
# t1.start()
# t2.start()

# import threading,time
# sum = 0
# def foo():
#     global sum
#     for i in range(10000):
#         time.sleep(0.001)
#         sum += i
#
# t1 = threading.Thread(target=foo)
# t2 = threading.Thread(target=foo)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print (sum)

# print (__file__)    #__file__  用来获得脚本所在的绝对路径
# #上面的打印结果是  G:/Python_scripts/Test/test_001.py
# import os
# print (os.getcwd())

# import time
# print (time.strftime('%Y-%m-%d-%H-%M-%S'))

# import os
# print (os.path.dirname(os.path.realpath(__file__)))

'''
from selenium import webdriver
import time

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get("https://m.weibo.cn/")

# 找到搜索输入框并点击
driver.find_element_by_class_name("m-search").click()
time.sleep(1)
# 找到 热搜榜所在大标签 card m-panel card16 m-col-2
hotSearchEle = driver.find_element_by_class_name("m-col-2")
# 在大标签中匹配热搜列表 m-item-box
hotSearchSli = hotSearchEle.find_elements_by_class_name("m-item-box")
# 取列表的最后一个元素,即微博热搜榜,并点击
hotSearchSli[-1].click()
time.sleep(1)
# 找到 实时热点，每分钟更新一次
hotSli = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div")

# 从 hotSli 中找到 card m-panel card4 标签列表, 即每一行热搜标签
hotDivSli = hotSli.find_elements_by_class_name("card4")
# 迭代 hotSli 中的每一个 div 标签  # 注: 第一个置顶的热搜不是每分钟更新一次, 每次刷新都可能不一样
for hotDiv in hotDivSli:
    # 判断这一行热搜有没有图片标签
    iconSli = hotDiv.find_elements_by_class_name("m-link-icon")
    if iconSli:  # 如果有图片标签
        # 获取 img 标签
        img = iconSli[0].find_element_by_tag_name("img")
        # 获取 src 属性
        srcLink = img.get_attribute("src")
        # 判断类型是 hot 还是 new 还是 fei
        if "hot" in srcLink:
            hotType = "热"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))
        elif "new" in srcLink:
            hotType = "新"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))
        elif "fei" in srcLink:
            hotType = "沸"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))

time.sleep(5)
driver.quit()
'''

print ('*'*10,'分隔符','*'*10)