from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,data):
        self.stack.append(data)
    def print(self):
        return self.stack
    def isEmpty(self):
        return len(self.stack)==0
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
stack =Stack()
val="{a+b}"
for i in val:
    if i=="(" or i=="{" or i=="["