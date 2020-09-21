# set 集合 frozenset (不可变集合)无序，不重复
s1 = set('abcdeerr')
print(s1)

s2 = set(['a','b','c','d','r','r','e','e','qq'])
print(s2)

s2.add('www')
print(s2)

s3 = {'a','b'}
print(type(s3))

# 不可变集合，定义后就不能动了，可以作为dict的key
s4 = frozenset('abcdefgg')
print(s4)

# 向set添加数据
another_set = set('erto76')
s3.update(another_set)
print(s3)