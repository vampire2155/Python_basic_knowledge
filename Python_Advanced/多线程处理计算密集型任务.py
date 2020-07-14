import threading,time

'''
计算密集型任务，是指CPU计算占主要的任务，CPU一直处于满负荷状态，不会存在CPU需要等待的情况。
比如计算 1 到无穷大 数的和（当然不存在这样的场景），复杂的加减乘除等。
'''
def foo(num):
    sum = 0
    for i in range(num):
        sum = sum + i

start_time = time.time()
#创建两个线程
t1 = threading.Thread(target=foo,args=[1000000])
t2 = threading.Thread(target=foo,args=[9999999])
#启动线程
t1.start()
t2.start()
#阻塞子线程的父线程
t1.join()
t2.join()

#以下是串行执行，总耗时：2.8511626720428467
# foo(1000000)
# foo(9999999)

end_time = time.time()
print (f'总耗时：{end_time-start_time}')  #并发执行，总耗时：2.8241615295410156

#所以对于 计算密集型任务，并发执行和 串行执行 耗时并 没有太大的区别。

# 从性能的角度考虑
#  **多线程**  适合IO密集型任务   只要在进行耗时的IO操作的时候，能释放GIL，所以只要在IO密集型的代码里，用多线程就很合适
#  **多进程**  适合计算密集型任务










