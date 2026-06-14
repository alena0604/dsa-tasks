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

    def preorder_traversal(self, index):
        # Time O(n)
        # Space O(n) - because recursive 
        if index > self.last_used_index:
            return
        print(self.custome_list[index])
        self.preorder_traversal(2*index)    # Time O(n/2)
        self.preorder_traversal(2*index + 1)


    def in_order_traversal(self, index):
        # left sub-tree -> root -> right sub-tree
        # Time O(n)
        # Space O(n) - because recursive 
        if index > self.last_used_index:
            return
        self.in_order_traversal(2*index)    # Time O(n/2)
        print(self.custome_list[index])
        self.in_order_traversal(2*index + 1)

    
    def post_order_traversal(self, index):
        # left sub-tree -> right sub-tree  -> root
        # Time O(n)
        # Space O(n) - because recursive 
        if index > self.last_used_index:
            return
        self.post_order_traversal(2*index)    # Time O(n/2)
        self.post_order_traversal(2*index + 1)
        print(self.custome_list[index])

    
    def level_order_traversal(self, index):
        # Time O(n)
        # Space O(1)
        for i in range(index, self.last_used_index + 1):
            print(self.custome_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There are no nodes to delete"
        for i in range(1, self.last_used_index + 1):
            if self.custome_list[i] == value:
                self.custome_list[i] = self.custome_list[self.last_used_index]
                self.custome_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been deleted"




new_bt = BinaryTree(8)
print(new_bt.insert_node("Drinks"))
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")

new_bt.level_order_traversal(1)
