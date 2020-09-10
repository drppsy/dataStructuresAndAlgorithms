import bisect

inter_list = []

bisect.insort(inter_list,3)
bisect.insort(inter_list,5)
bisect.insort(inter_list,2)
bisect.insort(inter_list,1)
bisect.insort(inter_list,6)

print(bisect.bisect(inter_list,3))

print(bisect.bisect_left(inter_list,3))

print(inter_list)


'''
也可以用deque的抽象数据结构，bobby有免费的collections的课程
'''