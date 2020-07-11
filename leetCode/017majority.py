class Solutions:

    def major1(self,nums):
        dict1 = {}
        for item in nums:
            dict1[item] = dict1.get(item,0) + 1
        return max(dict1,key=dict1.get)


def test_solutions():
    nums = [1,2,3,1,0]
    s = Solutions()
    print(s.major1(nums))

test_solutions()