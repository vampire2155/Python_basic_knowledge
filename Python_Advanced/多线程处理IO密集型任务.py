import threading,time

'''
什么叫IO密集型任务：IO 指的是input/output，即输入输出。 
是指磁盘IO、网络IO占主要，的任务，计算量很小。比如请求网页、读写文件等   **需要等待 响应返回**  的任务。
当然我们在Python中可以利用sleep达到IO密集型任务的目的。
'''

def foo(something):
    print (something)
    time.sleep(1)
start_time = time.time()
#创建两个线程
t1 = threading.Thread(target=foo,args=['发送接口请求'])
t2 = threading.Thread(target=foo,args=['等待接收接口返回并处理'])
#启动线程
t1.start()
t2.start()
#阻塞 子线程的 父线程，直到子线程 运行完成，才继续执行父线程
t1.join()
t2.join()

#以下是串行执行，总耗时：2.0001144409179688
# foo('发送接口请求')
# foo('等待接收接口返回并处理')

end_time = time.time()
print (f'总耗时：{end_time-start_time}')  #并发执行 总耗时：1.0020573139190674

#为什么 并发执行时间比 串行执行少呢？
# 因为并发执行时，CPU在等待响应的过程中立即去执行了另外一个线程的任务，而不是等待。
#而串行执行时，CPU则一直在等待 响应结束后 才开始执行另外一个线程的任务。



#  **多线程**  适合IO密集型任务
#  **多进程**  适合计算密集型任务