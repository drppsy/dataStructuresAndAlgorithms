def is_even(x):
    if x % 2 == 0:
        return x
    return


def get_even(x, y):
    even_list = []
    for i in range(x, y):
        if is_even(i):
            even_list.append(i)
    return even_list


# print(is_even(4))
print(get_even(1, 15))