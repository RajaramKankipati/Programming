class Stack:
    
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def getSize(self):
        return len(self.stack)


if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.getSize())
    print("Popped", stack.pop())
    print(stack.getSize())
    print(stack.stack)