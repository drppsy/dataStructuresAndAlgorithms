class A:
    cls_var = 1

    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(3,5)
print(a.x,a.y,a.cls_var)

A.cls_var = 10
print(a.x,a.y,a.cls_var)

a.cls_var = 100
print(a.x,a.y,a.cls_var)

b = A(2,6)
print(b.cls_var)