list1 = [2,4,5,7,8,9,]
list2 = [2,5,7]

# list3 = list(set(list1) - set(list2))

# print(list3)


list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)