class Array(object):

    def __init__(self,size=32):
        self.size = size
        self._items = [None]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self.size

    def clear(self,value=None):
        for i in range(0,len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class ArrayQueue(object):

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0
        self.array = Array(maxsize)

    def __len__(self):
        return self.head - self.tail

    def push(self,value):
        if len(self) >= self.maxsize:
            raise FullError("Queue Full")
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("Queue Empty")
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

def test_array_queue():
    maxsize = 3
    q = ArrayQueue(maxsize)
    q.push(1)
    q.push(2)
    q.push(3)

    assert len(q) == 3

    import pytest
    with pytest.raises(FullError) as excinfo:
        q.push(4)

    assert "Queue Full" == str(excinfo.value)

    q.pop()
    assert len(q) == 2

    q.push(4)
    len(q) == 3

    q.pop()
    q.pop()
    q.pop()

    with pytest.raises(EmptyError) as excinfo:
        q.pop()

    assert "Queue Empty" == str(excinfo.value)

test_array_queue()