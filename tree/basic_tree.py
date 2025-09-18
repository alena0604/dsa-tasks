# left child = cell[2*x]
# right child = cell[2*x + 1]


class BinaryTree:
    def __init__(self, size):
        self.custome_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        # Time O(1)
        # Space O(1)
        if self.last_used_index + 1 == self.max_size:
            return "full"
        self.custome_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "the value is added"

    def search_node(self, node_value):
        # Time O(n)
        # Space O(1)
        for i in range(len(self.custome_list)):
            if self.custome_list[i] == node_value:
                return "success"
        return "not found"



new_bt = BinaryTree(8)
print(new_bt.insert_node("Drinks"))
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
