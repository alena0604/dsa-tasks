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
        # insert at the end
        new_node = Node(value)  # O(1)
        if self.head is None:  # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            self.tail.next = new_node  # O(1)
            self.tail = new_node  # O(1)
        self.length += 1  # O(1)

    def prepend(self, value: int) -> None:
        # insert node to the beginning
        new_node = Node(value)  # O(1)
        if self.head is None:  # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            new_node.next = self.head  # O(1)
            self.head = new_node  # O(1)
        self.length += 1  # O(1)

    def insert(self, index, value) -> None | bool:
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            current = current.next

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def get(self, index):
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop_last(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index < -1:
            return self.pop_last()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        prev = None
        self.tail = self.head
        current = self.head
        while current:
            nxt = current.next
            current.next = prev  # flip pointer from next to prev
            prev = current  # assign prev for the iteration
            current = nxt   # 
        self.head = prev

     def find_middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.prepend(10)
    new_linked_list.append(20)
    new_linked_list.prepend(6)
    print(new_linked_list)
    print(new_linked_list.pop_first())
    print(new_linked_list)
