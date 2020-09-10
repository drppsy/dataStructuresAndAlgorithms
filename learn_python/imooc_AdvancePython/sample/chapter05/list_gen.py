# 列表生成式/列表推导式（即通过一行代码生成一个列表）
# 例如：提取出1-20之间的奇数
odd_list1 = []

for i in range(21):
    if i%2 == 1:
        odd_list1.append(i)

print(odd_list1)
print(isinstance(odd_list1,list))


odd_list2 = [i for i in range(21) if i%2 ==1]
print(odd_list2)
print(isinstance(odd_list2,list))


def handle_item(item):
    return item * item

odd_list3 = [handle_item(i) for i in range(21) if i%2 == 1]
print(odd_list3)
print(type(odd_list3))

'''
列表生成式的优点：
    列表生成式性能高于列表操作
'''

'''
生成器表达式
'''
odd_gen = (i for i in range(21) if i%2==1)
print(type(odd_gen))
# odd_list4 = list(odd_gen)
# print(odd_list4)
for item in odd_gen:
    print(item)


# 字典推导式
my_dict = {"feta":27,"niangao":2,"qiqi":1}
reversed_dict = {v:k for k,v in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {k for k in my_dict.keys()}
print(type(my_set))
print(my_set)

my_set2 = set(my_dict.keys())
print(my_set2)

