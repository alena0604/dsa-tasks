import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        # For undirected graph, also add: self.graph[v].append((u, weight))

    def dijkstra(self, start):
        # Priority queue (min-heap)
        pq = [(0, start)]  # (distance, node)
        distances = {start: 0}
        previous = {}

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            # Skip outdated entries
            if current_dist > distances.get(current_node, float('inf')):
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous


g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 6)
g.add_edge('C', 'D', 3)

distances, previous = g.dijkstra('A')
print(distances)

# {
#   'A': [('B', 1), ('C', 4)],
#   'B': [('C', 2), ('D', 6)],
#   'C': [('D', 3)],
#   'D': []
# }
