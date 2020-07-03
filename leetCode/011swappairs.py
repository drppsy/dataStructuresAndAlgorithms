class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self,head):
        pre,pre.next = self,head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b,a,b.next
            pre = a
        return self.next


def test_solution():
    head = ListNode(1)

    sec = ListNode(2)
    head.next = sec

    thr = ListNode(3)
    sec.next = thr

    four = ListNode(4)
    thr.next = four

    fiv = ListNode(5)
    four.next = fiv


    s = Solution()
    rfiv = s.swapPairs(head)

    print(rfiv.val)

    rfour = rfiv.next
    print(rfour.val)

test_solution()