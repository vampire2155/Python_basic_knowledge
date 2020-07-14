import threading,time
'''
同步锁的特点：
1、同步锁 也叫 互斥锁， 上锁 和 解锁  必须要对应，也就是说，上锁了以后 必须 进行 解锁 ，才能再次进行上锁操作。
2、如果上锁之后，不解锁，再次上锁，代码会阻塞。
3、如果解锁之后，在没有上锁的情况下再次解锁，代码会报错 （release unlocked lock）
'''
account = 500
lock = threading.Lock()  #申明一把锁
def foo(num):
    global account  #把account申明为全局变量，因为下面要改变account的值。
    lock.acquire()   #上锁，  同步锁 锁的是数据的操作。
    account_balance = account
    time.sleep(1)
    account_balance = account_balance + num
    account = account_balance
    lock.release()  #解锁
t1 = threading.Thread(target=foo,args=[10000])
t2 = threading.Thread(target=foo,args=[-300])
t1.start()
t2.start()
t1.join()
t2.join()
print (f'账户余额为：{account}')

#上述例子说GIL是失效的？ 是怎么判断出来的？？？？  判断依据：因为在没有 加同步锁的时候，每次运行结果都是不正确的。
# 这个失效的意思是：在这种情况下（在没有加同步锁的情况下） GIL 已经无法保证多线程共享数据安全。

# 由于 python 解释器（Cpython interpreter）不是线程安全（thread-safe）的，
# 所以 Cpython interpreter 的实现中使用了GIL（global interpreter lock)来阻止多线程同时在一个 pyobject 上操作。
# 按照上面这句话的意思是，GIL可以保证线程安全，但是为什么上面的例子 在不加 同步锁的时候，线程也是不安全（这里的不安全指的是 共享的数据不安全，
# 也就是说两个线程都操作全局变量account 的时候，计算结果是不正确的）的呢？ 答案是因为 在 上面的两个线程都共享了同一个 全局变量 account 资源，
# 并且 有了中间变量 account_balance 。因为两个线程都对自己内存里的 中间变量 account_balance 进行计算，然后最后又赋值给 全局变量 account。所以会导致计算结果不正确。


'''
# 如下例子在没有加 同步锁的时候，说明 多线程是 不安全的
# 两个线程同时对一个全局变量global_num = 0 进行1000000次global_num += 1 操作，正确的结果应该是global_num = 2000000 ，
# 但是在没有加同步锁的情况下，计算结果是不正确的。这就说明了  **多线程**  在共享数据时 是不安全的。
# 但是 这个不安全也是有前提的：就是  多个线程 都使用的是同一个 全局变量， 如果 每个线程都把全局变量赋值给另外的变量，并使用
import threading
global_num = 0
lock =threading.Lock()
def test1():
    global global_num
    lock.acquire()
    for i in range(1000000):
        global_num += 1
    lock.release()
    print("test1", global_num)

def test2():
    global global_num
    lock.acquire()
    for i in range(1000000):
        global_num += 1
    lock.release()
    print("test2", global_num)
t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)
t1.start()
t2.start()
'''


