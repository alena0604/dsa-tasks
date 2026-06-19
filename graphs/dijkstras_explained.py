# Dijkstra uses a min-heap (priority queue) to always pick the node with
# the smallest known distance. Once a node is picked from the heap,
# its distance is final — we've found the shortest path to it.
import heapq


def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {start: 0}
    previous = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > dist.get(current_node, float('inf')):
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_distance + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(heap, (new_dist, neighbor))

    return dist, previous


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('B', 1), ('D', 8)],
    'D': [],
}
print(dijkstra(graph, 'A'))