import sys
# list1 = [2,3,5,7,6,5,4,3,2]
#
# it = iter(list1)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
#
# for x in it:
#         print(x,end='  ')
#
#
# print('\n')
#

#
#
# '''
# 普通函数用 return 返回一个值，和 Java 等其他语言是一样的，然而在 Python 中还有一种函数，用关键字 yield 来返回值，这种函数叫生成器函数，函数被调用时会返回一个生成器对象，生成器本质上还是一个迭代器，也是用在迭代操作中，因此它有和迭代器一样的特性，唯一的区别在于实现方式上不一样，后者更加简洁
# '''
# def fab(n):
#     a,b,counter = 0,1,0
#     while counter <= n:
#         yield a
#         a,b = b,a+b
#         counter += 1
#
# f = fab(10)
#
# while True:
#     try:
#         print(next(f),end='  ')
#     except StopIteration:
#         sys.exit()


'''
器表达式和列表推导式
'''

g = (x**2 for x in range(10))
print(g)
print(type(g))

for x in g:
    print(x)

while True:
    try:
        print(next(g))
    except StopIteration:
        sys.exit()

l = [x**2 for x in range(10)]
print(l)
print(type(l))