
'''
看仔细了 是  多进程   而非  多线程。
经过试验证明：
**多线程**  适合IO密集型任务
**多进程**  适合计算密集型任务
'''


'''
import multiprocessing,time,threading
# 定义全局变量Queue
g_queue = multiprocessing.Queue()   #multiprocess.Queue是跨进程通信队列

def init_queue():
    print("init g_queue start")
    while not g_queue.empty():
        g_queue.get()
        for _index in range(10):
            g_queue.put(_index)
        print("init g_queue end")
        return

# 定义一个IO密集型任务：利用time.sleep()
def task_io(task_id):
    print(f"IOTask [{task_id}] start")
    while not g_queue.empty():
        time.sleep(1)
        try:
            data = g_queue.get(block=True, timeout=1)
            print(f"IOTask [{task_id}] get data: {data}")
        except Exception as excep:
            print(f"IOTask [{task_id}] error: {str(excep)}")
    print(f"IOTask [{task_id}] end")
    return

g_search_list = [i for i in range(10000)]  #使用列表生成式，创建一个列表。

# 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
def task_cpu(task_id):
    print(f"CPUTask [{task_id}] start")
    while not g_queue.empty():
        count = 0
        for i in range(10000):
            count += pow(3 * 2, 3 * 2) if i in g_search_list else 0
        try:
            data = g_queue.get(block=True, timeout=1)
            print(f"CPUTask [{task_id}] get data: {data}")
        except Exception as excep:
            print(f"CPUTask [{task_id}] error: {str(excep)}")
    print(f"CPUTask [{task_id}] end")
    return task_id


if __name__ == '__main__':
    print("cpu count:", multiprocessing.cpu_count(), "\n")

    print("========== 直接执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_io(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_io, args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_io, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 直接执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_cpu(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_cpu, args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行cpu密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_cpu, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：", time.time() - time_0, "\n")
'''

# 多进程处理计算密集型任务
import threading,time,multiprocessing

def foo(sum):
    sum = 0
    for i in range(sum):
        sum +=i

start_time = time.time()
#多线程  处理计算密集型任务
t1 = threading.Thread(target=foo,args=[9999999])
t2 = threading.Thread(target=foo,args=[8888888])
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print (f'多线程处理计算密集型任务耗时：{end_time-start_time}')

start_Ptime = time.time()
#多进程  处理计算密集型任务
p1 = multiprocessing.Process(target=foo,args=[9999999])
p2 = multiprocessing.Process(target=foo,args=[8888888])
p1.start()
p2.start()
p1.join()
p2.join()
end_Ptime = time.time()
print (f'多进程处理计算密集型任务耗时：{end_Ptime-start_Ptime}')

