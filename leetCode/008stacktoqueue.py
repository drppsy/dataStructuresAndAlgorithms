class Queue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self,x):
        return self.input_stack.append(x)

    def pop(self):
        if self.output_stack :
            return self.output_stack.pop()
        else:
            while self.input_stack:
                p = self.input_stack.pop()
                self.output_stack.append(p)
            if self.output_stack:
                return self.output_stack.pop()
            else:
                return -1

    def peek(self):
        if self.output_stack :
            return self.output_stack[len(self.output_stack)-1]
        else:
            while self.input_stack :
                p = self.input_stack.pop()
                self.output_stack.append(p)
        return self.output_stack[len(self.output_stack)-1]


def test_queue():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)

    assert q.pop() == 1
    assert q.pop() == 2
    q.pop()
    q.pop()
    q.pop()
    q.pop()


test_queue()




