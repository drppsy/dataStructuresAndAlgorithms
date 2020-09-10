# cpython中垃圾回收的算法，采用的是引用计数，变量每引用一次，计数+1，每del一次，计数-1，当减到0时，释放内存
a = object()
b = a
del a
print(b)
print(a)