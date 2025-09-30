# array-with-fixed-size style heap
# Parent: i // 2
# Left Child: 2 * i
# Right Child: 2 * i + 1


class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]


def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index, heap_type):
    # Time O(logN)
    # Space O(logN) - insert to stack memory
    if index <= 1:
        return
    parent_index = int(index/2)
    if heap_type == "min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            root_node.custom_list[index], root_node.custom_list[parent_index] = root_node.custom_list[parent_index], root_node.custom_list[index]
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            root_node.custom_list[index], root_node.custom_list[parent_index] = root_node.custom_list[parent_index], root_node.custom_list[index]
        heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value inserted"


def heapify_tree_extract(root_node, index, heap_type):
    # Time O(logN)
    # Space O(logN) - insert to stack memory
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == "min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                root_node.custom_list[index], root_node.custom_list[left_index] = root_node.custom_list[left_index], root_node.custom_list[index]
            return
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                root_node.custom_list[index], root_node.custom_list[left_index] = root_node.custom_list[left_index], root_node.custom_list[index]
            return

    else:
        if root_node.custom_list[index] > root_node.custom_list[right_index]: 
            swap_child = left_index
        else:
            swap_child = right_index
        if root_node.custom_list[index] < root_node.custom_list[swap_child]:
            root_node.custom_list[index], root_node.custom_list[swap_child] = root_node.custom_list[swap_child], root_node.custom_list[index]

    heapify_tree_extract(root_node, swap_child, heap_type)


def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extracted_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return extracted_node
   



new_heap = Heap(5)

insert_node(new_heap, 4, "max")
insert_node(new_heap, 5, "max")
insert_node(new_heap, 1, "max")
insert_node(new_heap, 3, "max")

level_order_traversal(new_heap)
    

