class EnqueueDequeue:
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

        if len(self.out_stack) == 0:
            raise IndexError("Empty stack!")

        return self.out_stack.pop()

stack = EnqueueDequeue()
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)

print(stack.dequeue())
print(stack.dequeue())
print(stack.dequeue())
print(stack.dequeue())