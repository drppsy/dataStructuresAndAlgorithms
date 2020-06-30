# # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head,None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


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
    rfiv = s.reverseList(head)
    rfour = rfiv.next
    assert rfour.val == 4

test_solution()