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

def level_order_traversal(root_node):
    # Time O(n)
    # Space O(n)
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)


def search_node(root_node, node_value):
     # Time O(logN)
    # Space O(logN)
    if root_node.data == node_value:
        return "Found"
    elif root_node.data > node_value:
        if root_node.left_child.data == node_value:
            return "Found"
        else:
            search_node(root_node.left_child, node_value)

    else:
        if root_node.right_child.data == node_value:
            return "Found"
        else:
            search_node(root_node.right_child, node_value)




new_bst = BSTNode(None)
print(insert_node(new_bst, 40))
print(insert_node(new_bst, 80))
print(insert_node(new_bst, 10))
print(insert_node(new_bst, 30))
print(insert_node(new_bst, 5))
print(new_bst.data)
print(new_bst.left_child.data)
print(new_bst.right_child.data)
print(search_node(new_bst, 10))