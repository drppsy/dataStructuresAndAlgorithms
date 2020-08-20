'''
2.1 python中的一切皆对象
    1. python的面向对象更彻底
    2. 函数和类也是对象，属于python的一等公民
        （1）可以赋值给一个变量
        （2）可以添加到集合对象中
        （3）可以作为参数给传递函数
        （4）可以当做函数的返回值
'''


# （1）可以赋值给一个变量
def ask(name="feta"):
    print(name)

my_func = ask
my_func("feta")

class Person:

    def __init__(self):
        print("niangao")

my_class = Person
my_class()

# （2）可以添加到集合对象中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in  obj_list:
    print(item())

# （3）可以作为参数给传递函数;（4）可以当做函数的返回值
def my_decorator():
    print("dec start")
    return ask

my_func3 = my_decorator()
my_func("zhuzhu")