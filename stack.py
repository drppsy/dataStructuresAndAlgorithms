class Node(object):

    def __init__(self,value = None, prev = None,next = None):
        self.value,self.prev,self.next = value,prev,next

class CircualBoubleLinkedList(object):

    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev,node.next = node,node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self,value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("Full")
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self,value):
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(value=value)

        if self.root.next is self.root: #空节点
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self,node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length += 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            return node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


class Deque(CircualBoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("Empty")
        value = self.tailnode()
        self.remove(value)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception("Empty")
        value = self.headnode()
        self.remove(value)
        return value


class Stack():

    def __init__(self):
        self.deque = Deque()

    def push(self,value):
        return self.deque.appendleft(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()

    for i in range(3):
        s.push(i)

    assert len(s) == 3

    assert s.pop().value == 0
    assert s.pop().value == 1
    assert s.pop().value == 2

test_stack()