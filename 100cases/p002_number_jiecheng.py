def cn(x):
    if x > 1:
        return x * cn(x-1)
    else:
        return 1

print(cn(3))
print(cn(4))
print(cn(6))