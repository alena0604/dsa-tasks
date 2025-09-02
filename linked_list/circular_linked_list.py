from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None  # Node or None for the end of the list


class CSLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:    # if it's empty node
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node       # added at the end
            self.tail = new_node
            new_node.next = self.head
        self.lenght += 1