import os

sum_of_size = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        sum_of_size += os.path.getsize(file)

print("sum_of_size:", sum_of_size/1000)