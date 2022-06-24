class Solution:
    def IntReverse(self,num):
        num_str_reverse = ""
        num_str = str(abs(num))
        if num < 0:
            for i in range(0,len(num_str)):
                reserve_index = len(num_str)-1-i
                num_str_reverse += num_str[reserve_index]
                num_int_reverse = -int(num_str_reverse)
                if num_int_reverse < (-2**33-1):
                    return 0
            return num_int_reverse
        else:
            for i in range(0,len(num_str)):
                reserve_index = len(num_str)-1-i
                num_str_reverse += num_str[reserve_index]
                num_int_reverse = int(num_str_reverse)
                if num_int_reverse > (2**33 - 1):
                    return 0
            return num_int_reverse

s = Solution()
print(s.IntReverse(109))
print(s.IntReverse(-392))

