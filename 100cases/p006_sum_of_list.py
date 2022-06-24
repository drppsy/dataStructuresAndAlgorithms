def get_sum_of_list(a_list):
    sum = 0
    for i in a_list:
        sum += i
    return sum


list1 = [2, 4, 6, 9, 10]
print(get_sum_of_list(list1))