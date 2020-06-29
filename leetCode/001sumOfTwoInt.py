# 暴力破解法，时间复杂度O(n^2)

# class Solution:
#     def twoSum(self,nums,target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#             return []
#
# nums = [7,2,8,13]
#
# # 排序+双指针
# class Solution:
#     def twoSum(self,nums,target):
#         temp = nums.copy()
#         temp.sort()
#         i = 0
#         j = len(nums)-1
#         while i < j:
#             if (temp[i] + temp[j]) > target:
#                 j -= 1
#             elif (temp[i] + temp[j]) < target:
#                 i += 1
#             else:
#                 break
#         p = nums.index(temp[i])
#         k = nums.index(temp[j])
#         if p == k:
#             return []
#         else:
#             return [p,k]
#
# s = Solution()
# print(s.twoSum(nums,10))


nums = [7,2,8,13]

class Solution:
    def twoSum(self,nums,target):
        aset = {}
        for i in  range(0,len(nums)):
            aset[nums[i]] = i
            if (target - nums[i]) in aset:
                return aset[target-nums[i]],i

s = Solution()
print(s.twoSum(nums,10))

adict = {"aa":"11","bb":"22"}
print(adict['aa'])