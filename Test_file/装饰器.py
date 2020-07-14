import time   #函数没有被调用  是不会执行的。
def foo():   #1、代码是从上到下依次执行，首先会执行到这里，但是这个是一个函数，并没有被调用，所以不会进入到函数内部
    print ('执行用例')
    time.sleep(1)
def show_time(func): #2、然后代码会执行到这里，但是这也是一个函数，并没有被调用，所以不会进入到函数内部
    def inner():   #这里的 inner()函数就是一个  装饰器。  装饰器返回值是一个 函数对象。
        begin_time = time.time()
        print ('begin_time:',begin_time)
        func()
        end_time = time.time()
        print ('end_time:',end_time)
        print ('执行用例总共运行时间：',end_time - begin_time)
    return inner
foo = show_time(foo) #3、代码执行到这里，然后调用了show_time()函数，函数名 foo是实参，
foo()



