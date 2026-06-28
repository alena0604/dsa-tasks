def bellman_ford(graph, vertices, source):
    # Step 1: Initialize distances
    distance = {v: float('inf') for v in range(vertices)}
    distance[source] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distance
