class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# class Solution:
#     def hasCycle(self,head:ListNode)-> bool:
#         fast = slow = head
#         while fast and slow and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False

class Solution:

    def swapPairs(self,head):
        pre,pre.next = self,head
        print(pre)
        print(pre.next.val)
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