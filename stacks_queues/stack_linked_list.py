from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None  # Node or None for the end of the list


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop_node(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def is_empty(self):
        if self.length == 0:
            return True

    def clear(self):
        self.top = None
        self.length = 0


m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
   m.pop_node()
   print(m.pop_node())