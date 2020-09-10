a = {"feta":{"company1":"dingdong"},"niangao":{"company2":"shuoye"}}

# a.clear()
# print(a)

# dict的copy方法，返回浅拷贝
# new_dict = a.copy()
# new_dict['feta']['company1'] = 'imooc'
# print(new_dict)
# print(a)


# 深拷贝
import copy

new_dict2 = copy.deepcopy(a)
new_dict2['feta']['company1'] = 'imooc'
print(new_dict2)
print(a)

# fromkeys

new_list = ['niangao','feta','zhuzhu','qiqi']
new_dict3 = dict.fromkeys(new_list,{"company":"imooc"})
print(new_dict3)