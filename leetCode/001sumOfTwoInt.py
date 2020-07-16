class Solutions:

    '''利用哈希表，哈希表的查询是O(1)时间复杂度，遍历整个数组是O(n)时间复杂度'''
    def twoSum1(self,nums,target):
        hasp_map = {}
        for i,x in enumerate(nums):
            if (target - x) in hasp_map:
                return [hasp_map[target-x],i]
            hasp_map[x] = i

    '''两层循环，时间复杂度是O(n)'''
    def twoSum2(self,nums,target):

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


def test_solutions():
    nums = [2,7,8,10]
    target = 9
    s = Solutions()
    res1 = s.twoSum1(target=target,nums=nums)
    print(res1)

    res2 = s.twoSum2(nums,target)
    print(res2)


test_solutions()

