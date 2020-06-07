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

def test_double_linked_list():
    dll = CircualBoubleLinkedList()
    dll.append(0)
    dll.append(1)

    assert len(dll) == 2

    dll.appendleft(2)
    assert len(dll) == 3

    assert [node.value for node in dll.iter_node()] == [2,0,1]
    assert [node.value for node in dll.iter_node_reverse()] == [1,0,2]

    headnode = dll.headnode()
    assert headnode.value == 2

    dll.remove(headnode)
    assert [node.value for node in dll.iter_node()] == [0,1]


test_double_linked_list()
