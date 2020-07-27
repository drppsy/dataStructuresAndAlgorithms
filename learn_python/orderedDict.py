list1 = [('aa','11'),('bb','22')]
print(list1)

dict1 = dict(list1)
print(dict1)


from collections import OrderedDict

dict2 = OrderedDict([('aa','11'),('bb','22')])
dict3 = OrderedDict([('bb','22'),('aa','11')])

print(dict1 == dict2)

print(dict2)
print(dict3)
print(dict2 == dict3)
