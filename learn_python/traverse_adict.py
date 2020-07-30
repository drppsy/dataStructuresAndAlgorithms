adict = {"aa":"11","bb":"22","cc":"33","dd":"44"}

# 遍历字典的key
for k in adict:
    print(k)

# 遍历字典的key，效果和上面一样
for k in adict.keys():
    print(k)

# 遍历字典的value
for value in adict.values():
    print(value)

# 遍历字典的key和value
for k,v in adict.items():
    print(k,v)