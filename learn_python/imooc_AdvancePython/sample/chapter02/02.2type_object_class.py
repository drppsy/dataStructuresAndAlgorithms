a = 1
# type这个类生成了int这个实例，int这个实例也是一个类，int这个类实例化生成了1这个实例
print(type(1))
print(type(int))

# type这个类生成了str这个类，str这个类实例化生成了"abc"
b = "abc"
print(type(b))
print(type(str))

# 类似的，type可以生成class，class实例化生成对象obj，例如下面这段代码
class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))

# python内建的类，数据类型
a = [1,2]
print(type(a))
print(type(list))

# object是最顶层基类
print(Student.__bases__)

class MyStudent(Student):
    pass

print(MyStudent.__bases__)

# type也是一个类，同时type也是一个对象，理解参考图
print(type.__bases__)
print(type(object))
print(object.__bases__)
