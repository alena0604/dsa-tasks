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
        for neighbor in graph.get(node, []):
            in_degree[neighbor] += 1

    # STEP 2: SEED push all in-degree 0 nodes
    queue = deque([i for i in range(n) if in_degree[i] == 0])

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

graph = {
 0: [1,2],
 1: [3,4],
 2: [5,6],
 3: [],
 4: [],
 5: [],
 6: []
}
print(topological_sort_kahn(graph, len(graph)))