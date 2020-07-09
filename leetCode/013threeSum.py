# map函数的用户，将一个可迭代的对象，放进一个函数里去（这个函数就是第一个参数）

class Solutions:

    def threeSum(self,nums):
        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i,v in enumerate(nums[:-2]):
            if i>=1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v,-v-x,x))
        return map(list,res)


def test_threeSum():
    nums = [-1,0,1,2,-1,-4]
    s = Solutions()
    alist = s.threeSum(nums)
    for item in alist:
        print(item)

test_threeSum()