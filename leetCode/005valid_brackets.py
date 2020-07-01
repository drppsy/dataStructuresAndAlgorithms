'''
基础知识：

'''
# adict = {"aa":"11","bb":"22","cc":"33"}
# # 字典的key可以用来做逻辑运算
# print('aa' in adict)
#
# # 字典的key可以用来取value
# print(adict['aa'])
#
# print('11' in adict)
#
# # 列表可以当做栈使用，列表有pop操作
# stack = ['aa','bb']
# # 列表pop方法，返回该pop的元素
# print(stack.pop())
# print(stack)

class Solution:
    def isValid(self,s):
        adict = {")":"(","]":"[","}":"{"}
        stack = []
        for c in s:
            if c in adict.values():
                stack.append(c)
            elif not stack or adict[c] != stack.pop() :
                return False
        return not stack

def test_solution():
    solu = Solution()
    strs = "(){}{}{({()})}[]"
    assert solu.isValid(strs) == 1

    strs = "(){}{}{({()})}[)]"
    assert solu.isValid(strs) == False

    strs = "(((()))"
    assert solu.isValid(strs) == False


test_solution()

