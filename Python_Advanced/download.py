import threading,time

def foo(something,num):
    for i in range(num):
        time.sleep(1)
        '''写上面这行代码的原因是 2个线程是并发执行，且因为 资源竞争，导致 2 个线程之间，
        其中一个线程还没有执行完，CPU就被另外一个线程抢走了，
        所以会出现 打印结果为  “CPU正在CPU正在  处理迅雷的任务处理Pycharm的任务”这样的情况。
        如何解决 资源竞争，这里就用到了 同步锁 。'''
        print ('CPU正在',something)
        time.sleep(1)  #写这行代码的原因与上面的一样。

t1 = threading.Thread(target=foo,args=['处理迅雷的任务',5])  #处理迅雷的任务 传给了foo函数中的something，5传给了num。
t2 = threading.Thread(target=foo,args=('处理Pycharm的任务',5))

t1.start()
t2.start()

