# Kahn's Algorithm
# COUNT: Count in-degrees for every node before you start
# SEED: Push all nodes with in-degree 0 into a queue
# POP: Dequeue a node. Add it to the result.
# PRUNE: For each neighbor: decrement its in-degree. If it hits 0, enqueue it.
from collections import deque


def topological_sort_kahn(graph, n):
    # graph[node] = list of neighbors (nodes it points to)
    # n = total number of nodes (0 to n-1)

    # STEP 1: COUNT in-degrees
    in_degree = [0] * n
    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # STEP 2: SEED push all in-degree 0 nodes
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # STEP 3 & 4: POP + PRUNE
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1 # prune the edge
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle check
    if len(result) != n:
        return []
    return result