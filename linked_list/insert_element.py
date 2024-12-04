class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
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
    print(new_linked_list.length)
    print(new_linked_list.head.value)
