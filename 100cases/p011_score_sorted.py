list1 = [{"sno": "101", "sname": "小张", "sgrade": "88"}, {"sno": "102", "sname": "小王", "sgrade": "77"},
         {"sno": "103", "sname": "小李", "sgrade": "99"}, {"sno": "104", "sname": "小赵", "sgrade": "66"}]

# a_dict = {}
# for i in list1:
#     a_dict[i['sgrade']] = i
#
# list2 = []
# for i in sorted(a_dict, reverse=True):
#     list2.append(a_dict[i])
#
# print(list2)

list2 = sorted(list1, key=lambda x: x['sgrade'], reverse=True)
print(list2)