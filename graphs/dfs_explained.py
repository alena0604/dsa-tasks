# Deep first search
# recursive

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()     # initialize

    visited.add(node)
    print(f"Visiting: {node}")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)   # Go deep into each neighbor


graph = {0:[1,2], 1:[0,3,4], 2:[0,5,6], 3:[1], 4:[1], 5:[2], 6:[2]}
print(dfs(graph, 0))