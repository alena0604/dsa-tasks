class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def push(self, element):
        self.items.append(element)

    def peak(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]



new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
print(new_stack)
new_stack.pop()
print(new_stack)