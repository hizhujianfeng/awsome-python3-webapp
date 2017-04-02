#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多进程、多线程

unix/linux fork()实现多进程

跨平台多进程：multiprocessing

进程间通信：Queue、Pipes
"""
from multiprocessing import Process, Pool, Queue
import os, time, random
import subprocess
import threading


# 子进程通过getpid()父进程的ID Unix/Linux系统可用
# print('Process (%s) start ...' % os.getpid())
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just  created  a child process (%s). ' % (os.getpid(), pid))


# windows 可以用multiprocessing模块  实现多进程：子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start .')
#     p.start()
#     p.join()
#     print('Child process end .')
#
#
# # 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # 默认是4,4核cpu
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done ...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

#子进程
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code ', r)

#这些代码报错
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
"""
进程间通信
"""


# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()


"""
多线程

_thread  低级模块
threading 高级模块

"""


# 新线程执行代码
# def loop():
#     print('thread %s is running ...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('%s' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# lock
# 多进程中，同一个变量，各自有一份拷贝存在于每一个进程中
# 多线程中,所有变量都由所有线程共享


balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()


def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
