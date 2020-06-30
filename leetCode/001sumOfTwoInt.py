class Solution:
    def twoSum(self,nums,target):
        hash_map = dict()
        for i,x in enumerate(nums):
            if target-x in hash_map:
                return [hash_map[target-x],i]
            hash_map[x] = i

def test_solution():
    s = Solution()

    nums = [3, 5, 9]
    print(s.twoSum(nums,8))

    nums = [3, 3, 9]
    print(s.twoSum(nums,6))

test_solution()