import heapq


class Solutions:

    def maxSlidingWindow1(self,nums,k):
        if not nums:
            return []
        res = []
        for i in range(k,len(nums)+1):
            slush_heap = heapq.nlargest(k,nums[i-k:i])
            res.append(slush_heap[0])
        return res

    def maxSlidingWindow2(self,nums, k):
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


def test_solutions():
    alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 12, 45, 13, 24]

    s = Solutions()
    res = s.maxSlidingWindow1(alist,3)
    print(res)

    alist = []
    res = s.maxSlidingWindow1(alist,0)
    print(res)

    alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 12, 45, 13, 24]
    res = s.maxSlidingWindow2(alist,3)
    print(res)

    alist = []
    res = s.maxSlidingWindow2(alist,0)
    print(res)

test_solutions()