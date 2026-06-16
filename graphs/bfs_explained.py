# 1 Start at a node. Mark it visited. Add it to the queue.
# 2 Take the FRONT item from the queue. Process it.
# 3 Add all its UNVISITED neighbors to the BACK of the queue. Mark them visited.
# 4 Repeat from step 2 until queue is empty.
from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        for neighbours in graph[current_node]:
            if neighbours not in visited:
                visited.add(neighbours)
                queue.append(neighbours)

    return result


graph = {0:[1,2], 1:[0,3,4], 2:[0,5,6], 3:[1], 4:[1], 5:[2], 6:[2]}
print(bfs(graph, 0))