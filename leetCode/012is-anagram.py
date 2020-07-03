class Solutions:

    def is_anagram1(self,s,t):
        return  sorted(s) == sorted(t)

    def is_anagram2(self,s,t):
        dict1,dict2 = {},{}
        for item in s:
            dict1[item] = dict1.get(item,0) + 1
        for item in t:
            dict2[item] = dict2.get(item,0) + 1
        return dict1 == dict2


def test_solutions():
    s = 'act'
    t = 'cat'

    so1s = Solutions()
    assert so1s.is_anagram1(s, t) == True

    assert so1s.is_anagram2(s, t) == True


test_solutions()