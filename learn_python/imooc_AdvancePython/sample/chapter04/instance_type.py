'''
isinstance会去沿着继承关系链去查找某个值是否属于某个类型，尽量用isinstance，少用type,type得出的是一个对象，对象id之间比较不一定准确，
is比较的是对象id、内存地址；==比较的是两个值
'''

a = 1
b = 1

print(a is b)
print(a == b)


class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(type(b) is A)
print(type(b) == A)