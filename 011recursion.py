from collections import deque

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def test_fact():
    a = fact(10)
    print(a)

test_fact()

class Stack():
    def __init__(self):
        self.stac = deque()

    def push(self,n):
        return self.stac.append(n)

    def pop(self):
        return self.stac.pop()

    def is_empty(self):
        return len(self.stac) == 0

def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())

print_num_use_stack(10)


# def Fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return Fib(n-1)+Fib(n-2)
#
# f = Fib(30)
# print(f)