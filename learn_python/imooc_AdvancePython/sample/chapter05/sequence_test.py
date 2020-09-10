'''
序列类型的分类
1. 容器类型
    list、tuple、deque
2. 扁平类型
    str、byte、bytearray、array.array
3. 可变序列
    list、deque、bytearray、array
4. 不可变序列
    str、tuple、bytes


数组和列表的区别：
    数组在声明的时候，会规定它的数据类型；列表里面的元素可以是不同的数据类型
'''


my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc


a = [1,2]

c = a + [3,4]

print(c)

a += [3,4]
print(a)

a += (5,6)
print(a)

a.extend(range(3))
print(a)

a.extend((7,8,9))
print(a)

a.append((7,8,9))
print(a)

a.append([7,8,9])
print(a)