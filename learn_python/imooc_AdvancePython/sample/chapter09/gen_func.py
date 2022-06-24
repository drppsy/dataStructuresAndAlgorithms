# 生成器函数，函数里只要有yeild关键字
# 为惰性求值，延迟求值提供了可能
def gen_func():
    yield 1
    yield 2
    yield 3


def func():
    return 1

# 斐波那契数列
def fib(index):
    fib_list = [1]
    n,a,b = 0,0,1
    while n < index:
        a,b = b,a+b
        n += 1
        fib_list.append(b)
    return fib_list

def gen_fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        n += 1


if __name__=="__main__":
    # 生成器函数，返回的是一个生成器对象。python编译字节码的时候就产出了
    # gen = gen_func()
    # for value in gen:
    #     print(value)
    # re = func()
    # fib_list = fib(20)
    # print(fib_list)
    for data in gen_fib(10):
        print(data)

