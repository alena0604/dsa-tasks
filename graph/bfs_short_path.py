from collections import defaultdict, deque



class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict()
        self.gdict = gdict

    def bfs_short_path(self, start, end):
        # Time O(E)
        # Space O(E)
        # unweighted graph
        queue = deque(start)
        queue.append(start)
        while queue:   # O(V)
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return path

            for adjacent in self.gdict.get(node, []):  # O(E)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


new_dict = {'a': ['b', 'c'], 
            'b': ['d', 'g'], 
            'c':['d', 'e'], 
            'd': ['b', 'f'],
            'e': ['c', 'f'],
            'g': ['b', 'f']}
print(new_dict.get("z", []))

graph = Graph(new_dict)
print(graph.bfs_short_path("a", "e"))