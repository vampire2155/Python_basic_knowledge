import time
import threading
def foo(something):
    for i in range(10):
        time.sleep(1)
        print (something)
#创建线程   --本质是 创建了一个实例，因为 Thread() 是一个类。
t1 = threading.Thread(target=foo,args=('看电影',))
t2 = threading.Thread(target=foo,args=('听音乐111111',))

#声明守护线程
t1.setDaemon(True)
# t2.setDaemon(True)
#启动线程
t1.start()    #start() 是 Thread() 类中的一个方法。
t2.start()
#阻塞线程
# t1.join()
for i in range(5):
    time.sleep(1)
    print ('消费数据')
print ('结束了------------------------')


threading.RLock()
