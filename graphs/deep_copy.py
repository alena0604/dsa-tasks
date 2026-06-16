from collections import deque


def deep_copy(adj: dict[int: list[int]]):
    cloned = {}
    for node in adj:
        dfs(adj, node, cloned)
    return cloned

def dfs(adj, node, cloned):
    if node in cloned:
        return
    cloned[node] = []
    for neighbour in adj[node]:
        dfs(adj, neighbour, cloned)
        cloned[node].append(neighbour)


def deep_copy_bfs(adj: dict[int, list[int]], start):
    cloned = {start: []}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in adj[node]:
            if neighbour not in cloned:
                cloned[neighbour] = []
                queue.append(neighbour)
            cloned[node].append(neighbour)
    return cloned


# print(deep_copy({'a': ['b', 'c'], 'b': ['a', 'd'], 'c':['a'], 'd': ['b']}))

print(deep_copy_bfs({'a': ['b', 'c'], 'b': ['a', 'd'], 'c':['a'], 'd': ['b']}, "a"))