# 操作系统原来能够调度的最小单元是进程，一个进程可以看做是一个正在执行的程序，但因为进程消耗资源比较大，因此逐步演变成操作系统能够调度的最小
# 单元是线程，线程是基于进程的，一个进程可以有多个线程，

# 对于io操作来说，多线程和多进程性能差别不大
# 1. 通过Thread类实例化，

import time
import threading

def get_detail(url):
    print('get html detail start')
    time.sleep(2)
    print('get html detail end')

def get_list(url):
    print('get list start')
    time.sleep(2)
    print('get list end')

if __name__ == "__main__":
    pass