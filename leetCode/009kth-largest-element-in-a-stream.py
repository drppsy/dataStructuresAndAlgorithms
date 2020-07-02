import heapq


class KthLargest():

    def __init__(self,k,nums):
        self.k,self.kheap = k,heapq.nlargest(k,nums + [float('-inf')])
        heapq.heapify(self.kheap)

    def add(self,val):
        heapq.heappushpop(self.kheap,val)
        return self.kheap[0]

def test_kthlargest():
    alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 12, 45, 13, 24]
    h = KthLargest(7,alist)

    assert h.add(6) == 7
    assert h.add(9) == 8


test_kthlargest()