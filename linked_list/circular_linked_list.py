from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None  # Node or None for the end of the list

    def __str__(self) -> str:
        return str(self.value)  # Convert the value to a string


class CSLinkedList:
    def __init__(self):
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
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length +=1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search_node(self, target):
        current = self.head
        while current is not Node:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


cs_linked_list = CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.prepend(50)
cs_linked_list.insert(0, 3)
print(cs_linked_list.search_node(30))
print(cs_linked_list)
