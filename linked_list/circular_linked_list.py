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

    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.tail = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop_node(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index < -1:
            return self.pop_node()
        prev_node = self.get_node(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        if not self.head:
            return None
        if self.length == 1:
            if self.head.value == value:
                self.head = None
                self.tail = None
                self.length -=1
                return True
            return False
        current = self.head
        if self.head.value == value:
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return True
        while current.next != self.head:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current 
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def is_sorted(self):
        if not self.head or not self.head.next:
            return True
        current = self.head
        while current.next != self.head:
            if current.value >= current.next.value:
                return False
            current = current.next
        return True


cs_linked_list = CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.prepend(50)
cs_linked_list.insert(0, 3)
print(cs_linked_list.search_node(30))
print(cs_linked_list)
cs_linked_list.pop_node()
print(cs_linked_list)

