class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    # Time O(logN)
    # Space O(logN)
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


def pre_order_traversal(root_node):
    # Time O(n)
    # Space O(n)
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    # Time O(n)
    # Space O(n)
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    # Time O(n)
    # Space O(n)
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


new_bst = BSTNode(None)
print(insert_node(new_bst, 40))
print(insert_node(new_bst, 80))
print(insert_node(new_bst, 10))
print(new_bst.data)
print(new_bst.left_child.data)
print(new_bst.right_child.data)