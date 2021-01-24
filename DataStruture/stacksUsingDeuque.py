from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,data):
        self.stack.append(data)
    def print(self):
        print(self.stack)
    def isEmpty(self):
        print(len(self.stack)==0)
    def peek(self):
        print(self.stack[-1])
stack=Stack()
stack.push(99)
stack.push(99)
stack.push(99)
stack.isEmpty()
stack.peek()
stack.print()