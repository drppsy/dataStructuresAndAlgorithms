class Solutions:

    def strSort(self,s):
        hash_map = {}
        for c in s:
            hash_map[c] = hash_map.get(c,0) + 1
        res = sorted(hash_map.items(),key= lambda item:item[1],reverse = True)
        return res


def test_strSort():
    s = 'aaffdffwwwweererwwwegfg'
    so = Solutions()
    res = so.strSort(s)
    print(res)

test_strSort()