'''
python中的常见内置类型
    1. 对象的三个特征
        （1）身份：对象在内存中的地址。对象是存在内存当中的，通过身份这个指针，指向内存地址的这个对象。可以通过id()这个方法知道对象的身份
        （2）类型
        （3）值
    2. None全局只有一个
    3. 数值
        (1)int
        (2)float
        (3)complex(复数）
        (4)bool
    4. 迭代类型
    5. 序列类型
        (1)list
        (2)range
        (3)tuple
        (4)str
        (5)array
        (6)bytes、bytearray、memoryview( 二进制序列)
    6. 映射（dict/map)
    7. 集合
        (1)set
        (2)frozenset
    8. 上下文管理类型(with)
    9. 其他
        (1)模块类型
        (2)class和实例
        (3)函数类型
        (4)方法类型
        (5)代码类型
        (6)object对象
        (7)type类型
        (8)ellipsis类型 '省略号类型'
        (9)notimplemented类型
'''

# 对象的身份/id
a = 1
print(id(a))

# None全局只有一个，python解释器在初始化的时候会生成一个全局的None对象
b = None
c = None
assert id(b) == id(c)