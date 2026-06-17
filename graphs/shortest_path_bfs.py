from collections import deque


def shortest_path_bfs(graph, start, end):
    if start == end:
        return [start]

    visited = {start}
    queue = deque([[start]])  # stores path as []
    while queue:
        path = queue.popleft()
        node = path[-1]     # current node is the last in the path [0, 1 ...]

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path
                visited.add(neighbor)
                queue.append(new_path)

    return []


graph = {0:[1,2], 1:[0,3,4], 2:[0,5,6], 3:[1], 4:[1], 5:[2], 6:[2]}
print(shortest_path_bfs(graph, 0, 5))