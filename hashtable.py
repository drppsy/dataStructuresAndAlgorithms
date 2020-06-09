class Array(object):

    def __init__(self,size=32,init=None):
        self.size = size
        self._items = [init]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self.size

    def clear(self,value=None):
        for i in range(0,len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):
    UNUSED = None   #槽没有被使用
    EMPTY = Slot(None,None)   #槽被使用过，但已经被移除/删除

    def __init__(self):
        self._table = Array(size=8,init=HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    #@property装饰器，把一个方法变成属性使用
    @property
    def _load_factor(self):
        return self.length/float(len(self._table))

    def _hash(self,key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 +1) % _len
            elif self._table[index] == key:
                return index
            else:
                index = (index*5 +1) % _len
        return None
