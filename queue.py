# 定义节点类，节点类包含value和指向下一个值的指针
class Node(object):

    def __init__(self,value = None, next = None):
        self.value,self.next = value,next


class LinkedList(object):

    # next=None代表链表可以默认无限扩容
    def __init__(self,maxsize = None):
        # 定义链表的大小
        self.maxsize = maxsize
        # 定义空节点作为根节点
        self.root = Node()
        # 定义初始长度是0
        self.length = 0
        # 定义空节点作为尾节点初始值
        self.tailnode = None

    # 定义LinkedList的len方法
    def __len__(self):
        return self.length

    # 定义增加节点的方法，value所增加node的值
    def append(self,value):
        # 如果链表不是无限扩容的，并且链表的长度已经等于了最长长度，那么抛出异常
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Full")

        # 将Node，值为value
        node = Node(value)
        # 定义尾节点，默认值是默认值None
        tailnode = self.tailnode

        # 如果尾节点是None，说明这是一个空链表，因此空链表的根节点的下一个节点，就可以赋值为node，并且把增加的节点设置为尾节点
        if tailnode is None:
            self.root.next = node
        # 如果尾节点不是None，说明这不是空链表，那么就可以把当前的尾节点的前驱指针指向增加的这个节点，并且把增加的节点设置为尾节点
        else:
            tailnode.next = node
        # 不管当前链表是否是空链表，当需要把增加的节点赋值给尾节点，因此下一行代码放在if、else整个代码块后面
        self.tailnode = node
        # 增加成功后，长度+1
        self.length += 1

    # 定义向左插入一个节点的方法
    def appendleft(self,value):
        # 将需要插入的值实例化成一个节点
        node = Node(value)
        # 定义头结点，即根节点的下一个节点
        headnode = self.root.next
        # 将当前插入的节点放在根节点的后面
        self.root.next = node
        # 将当前插入节点的前驱指针指向头结点
        node.next = headnode
        # 增加成功后，长度+1
        self.length += 1

    # 增加LinkedList的迭代方法
    def iter_node(self):
        # 将根目录的下个节点赋值给当前节点，每次迭代都是从第一个节点开始迭代
        curnode = self.root.next
        # 当 当前节点不是None的时，yield当前节点，并把当前节点的下一个节点赋值给当前节点
        while curnode is not None:
            yield curnode
            curnode = curnode.next
        # 当 当前节点是None，仍然yield当前节点
        # yield curnode

    # 定义LinkedList的删除一个值的方法
    def remove(self,value):
        # 将根节点设置为默认的上一个节点
        prevnode = self.root
        # 将根节点的下一个节点设置为当前节点
        curnode = self.root.next

        # 迭代LinkedList的所有节点
        for curnode in self.iter_node():
            # 如果当前节点的值等于需要删除的值，那么，将前一节点的前驱指针指向当前节点的下一个节点
            if curnode.value == value:
                prevnode.next = curnode.next
                # 如果当前节点正好是尾节点，那么将前一节点设置为尾节点
                if curnode == self.tailnode:
                    self.tailnode = prevnode
                # 不管当前节点是不是尾节点吗，都删除掉节点的value等于所输入value的节点
                del curnode
                # 长度-1
                self.length -= 1
                # 删除成功，返回1
                return 1
            # 如果当前节点的值不等于需要删除的值，那么将当前节点的值赋值给前一节点
            else:
                prevnode = curnode
        # 如果不是返回1，那么返回-1，作为删除失败
        return -1

    # 查找节点值和value匹配的节点的位置/索引
    def find(self,value):
        # 定义初始索引为0
        index = 0
        # 遍历链表的节点
        for node in self.iter_node():
            # 如果节点值和输入值匹配,则返回该索引
            if node.value == value:
                return index
            # 如果值不匹配,则每遍历一次,index+1
            index += 1
        # 如果没找到该value,则返回-1
        return -1

    # 向左pop一个
    def popleft(self):
        headnode = self.root.next
        if headnode is None:
            raise Exception("这是一个空节点")
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None


class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class Queue(object):

    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self,value):
        if self.maxsize is not None and len(self)>= self.maxsize:
            raise FullError("Queue Full")
        return self._item_linked_list.appendleft(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("Queue Empty")
        return self._item_linked_list.popleft()


def test_queue():
    q = Queue(maxsize=3)
    q.push(1)
    q.push(2)
    q.push(3)

    assert len(q) == 3

    import pytest
    with pytest.raises(FullError) as excinfo:
        q.push(4)

    assert "Queue Full" == str(excinfo.value)

    q.pop()
    assert len(q) == 2

    q.pop()
    q.pop()

    with pytest.raises(EmptyError) as excinfo:
        q.pop()

    assert "Queue Empty" == str(excinfo.value)

test_queue()

