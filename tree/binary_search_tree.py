class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)
    return "success"


new_bst = BSTNode(None)
print(insert_node(new_bst, 40))
print(insert_node(new_bst, 80))
print(insert_node(new_bst, 10))
print(new_bst.data)
print(new_bst.left_child.data)
print(new_bst.right_child.data)