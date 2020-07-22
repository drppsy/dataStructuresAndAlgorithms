import time
# 装饰器经常用来搭配使用的模块和包
from functools import wraps

# 装饰器的本质就是把函数名作为一个参数传入装饰函数，装饰函数会返回一个新的函数名或调用函数，在新的函数名里进行被装饰函数本身的功能逻辑。
# 下面这个函数是测试函数的运行时间的，常用来测试请求时间
def runTime(func):
    @wraps(func)
    def func_run_time(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        return total_time,res
    return func_run_time

# @是装饰一个函数的快捷方法，@后该函数就成为了被装饰函数
@runTime
def bubleSort(arr):
    num = len(arr)
    for i in range(num):
        for j in range(num - i -1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    time.sleep(1)
    return arr

# 运行过程是，（1）将buble函数名传递给runTime函数，runTime函数返回func_run_time函数名，因为后面有（），所以func_time_time函数被调用，执行该函数名下面的代码逻辑
arr = [45,7,2,24,32,9,10,28]
a = bubleSort(arr)
print(a)



# 打印日志的函数
def logit(logfile='out.log'):
    def log_decorator(func):
        @wraps(func)
        def wrap_func(*args,**kwargs):
            log_detail = func.__name__ + " was called"
            print(log_detail)
            with open(logfile,'a') as logs:
                logs.write(log_detail + '\n')
            return func(*args,**kwargs)
        return wrap_func
    return log_decorator


# 因为是logit调用的真正装饰器函数，因此下面的代码需要加（），要不要括号（），就看函数本身是不是真正的装饰器函数，还是函数内调用装饰器函数（这种情况需要括号）。
@logit()
def fun1():
    pass

fun1()