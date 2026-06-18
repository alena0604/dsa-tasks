# Counting connected components. If the graph isn't fully connected, some nodes can't reach others.
# Each "island" of reachable nodes is a connected component.
# T - O(V + E), S - O(V)

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def count_components(graph):    # has recursion limit
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1
    return count


graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    # ─────── gap ───────
    3: [4],    # Node 3 can't reach 0, 1, or 2
    4: [3],
}
print(count_components(graph))
