class Stack:
    
    def __init__(self):
        self.stack=[]
        self.n=11
    def push(self,value):
        if len(self.stack)==self.n:
            self.isFull()
        else:
            self.stack.append(value)
    def print(self):
        print(self.stack)
    def isEmpty(self):
        if len(self.stack)==0:
            print("It is Empty")
        else:
            print("It is not empty")
    def peek(self):
        return self.stack[-1]
    def pop(self):
        self.stack.pop()
    def isFull(self):
        if len(self.stack)==self.n:
           print("List is Full")
stack=Stack()
for i in range(1,10):
    stack.push(i)
stack.push(18)
stack.push(98)
stack.push(240)
stack.print()
stack.isFull()
stack.peek()