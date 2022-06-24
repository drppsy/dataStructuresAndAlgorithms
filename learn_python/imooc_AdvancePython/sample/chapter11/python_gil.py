# gil global interpreter lock （cpython）
# python中的一个线程对应于c语言中的一个线程
# gil使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行.
# 值得注意的是，gil会根据执行的字节码行数以及时间片释放gil，gil还会在遇到io操作时，主动释放
# io操作，input、output操作，人与计算机之间的信息交换，例如敲击键盘输入信息，从电脑磁盘中输出信息等

# import dis
# def add(a):
#     a += 1
#
# print(dis.dis(add))

total = 0

# case1,内存小的情况下的gil:
def add():
    global total
    for i in  range(100):
        total += 1


def desc():
    global total
    for i in range(100):
        total -= 1

import threading
threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)

threading1.start()
threading2.start()

threading1.join()
threading2.join()
print(total)


# case2，内存大的情况下的gil，gil并非一直被某个线程占用，对应线程结束完后才会执行，而是会根据字节码执行的行数做调整，行数超过一定量时，gil
# 会释放出来，给下一个线程运行:

def add():
    global total
    for i in  range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)

threading1.start()
threading2.start()

threading1.join()
threading2.join()
print(total)
