def sum_of_nn(n):
    if n > 1:
        return pow(n, 2) + sum_of_nn(n-1)
    else:
        return 1


print(sum_of_nn(5))

