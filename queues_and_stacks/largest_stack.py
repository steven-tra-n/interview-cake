class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        if self.max_stack.peek() == None or self.max_stack.peek() <= item:
            self.max_stack.push(item)

    def pop(self):
        if self.stack.peek() == self.max_stack.peek():
            self.max_stack.pop()

        return self.stack.pop()

    def get_max(self):
        return self.max_stack.peek()

result = MaxStack()
result.push(5)
result.push(4)
result.push(6)
result.push(3)

result.pop()
result.pop()
result.pop()
result.pop()

print(result.get_max())