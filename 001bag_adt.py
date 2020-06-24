class Bag(object):

    def __init__(self,maxsize=10):
        # 定义背包的最大容量
        self.maxsize = maxsize
        # 定义容器的类型，选择列表list作为容器
        self._items = list()
    # 定义Bag这一抽象数据类型的增加元素的方法add，如果Bag超过10个，则报错"Bag is Full"。注：列表list这一容器有append()这一方法
    def add(self,item):
        if len(self._items) > self.maxsize:
            raise Exception("Bag is Full")
        self._items.append(item)

    # 定义Bag这一抽象数据类型的删除元素的方法remove。注：列表list这一容器有remove()这一方法
    def remove(self,item):
        self._items.remove(item)

    # 定义Bag这一抽象数据类型的计算长度方法len。注：列表list这一容器有len()这一方法，但不写下面这段代码，Bag本身是没有这个方法的，因此需要在这里定义Bag的len()方法，且下面def__len__(self)的写法不能变，其他写法会有问题。
    def __len__(self):
        return len(self._items)

    # 定义Bag这一抽象数据类型的迭代方法，使之成为可迭代的对象。注：不写下面这段代码，Bag是不可迭代的对象，因此需要在这里定义Bag的迭代方法，且下面def__iter__(self)的写法不能变，其他写法会有问题。
    def __iter__(self):
        # for + yield的用法，使某个ADT成为可迭代的对象
        for item in self._items:
            yield item

# 以下是单元测试代码
def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)

test_bag()
