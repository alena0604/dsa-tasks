from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None  # Node or None for the end of the list

    def __str__(self) -> str:
        return str(self.value)  # Convert the value to a string


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None  # Head can be None initially
        self.tail: Optional[Node] = None  # Tail can be None initially
        self.length: int = 0

    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    def append(self, value: int) -> None:
        new_node = Node(value)  # O(1)
        if self.head is None:  # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            self.tail.next = new_node  # O(1)
            self.tail = new_node  # O(1)
        self.length += 1  # O(1)


if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.append(10)
    new_linked_list.append(20)
    print(new_linked_list)
