class Solution:
    def longest(self,strs):
        strs_sorted = sorted(strs,key= lambda i:len(i),reverse=False)
        shortest_str = strs_sorted[0]
        shortest_str_len = len(shortest_str)
        for i in range(0,shortest_str_len):
            public_str_prefix = shortest_str[0:shortest_str_len-i]
            j = 1
            while j < len(strs):
                if public_str_prefix == strs_sorted[j][0:shortest_str_len-i]:
                    j += 1
                else:
                    break
            if j == len(strs):
                return public_str_prefix
        return None

def test_solution():
    strs = ['aabb','aab','aabc','aabc','aabd']
    s = Solution()
    print(s.longest(strs))

test_solution()