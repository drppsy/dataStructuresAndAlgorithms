# import heapq
# class SlushLargest():
#
#     def get_kmax(self,k,nums):
#         if not nums:
#             return []
#         else:
#             max_nums = []
#             for i in range(k,len(nums)+1):
#                 slush_heap = heapq.nlargest(k,nums[i-k:i])
#                 max_nums.append(slush_heap[0])
#             return max_nums
#
# def test_slushlargest():
#     alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 12, 45, 13, 24]
#     s = SlushLargest()
#     max_nums = s.get_kmax(3,alist)
#     print(max_nums)
#
#     alist = []
#     max_nums = s.get_kmax(0,alist)
#     print(max_nums)
# test_slushlargest()

nums = [1, 2, 7, 5, 8]

def maxSlidingWindow1(nums,k):
    if not nums: return []
    window, res = [],[]
    for i,x in enumerate(nums):
        if i >= k and window[0] <= i -k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res

m = maxSlidingWindow1(nums,3)
print(m)
