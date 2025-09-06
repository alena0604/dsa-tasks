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

    def push(self, element):
        self.items.append(element)



new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
print(len(new_stack.items))