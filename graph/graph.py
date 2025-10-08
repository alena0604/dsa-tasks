# A defaultdict automatically creates a default value for any key that doesn’t exist.

# from collections import defaultdict

# graph = defaultdict(list)

from collections import deque


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        if vertex in self.gdict:
            self.gdict[vertex].append(edge)
        else:
            self.gdict[vertex] = [edge]

    def remove_edge(self, vertex, edge):
        if vertex in self.gdict:
            try:
                self.gdict[vertex].remove(edge)
            except ValueError:
                pass

    def remove_vertex(self, vertex):
        if vertex in self.gdict.keys():
            for ver in self.gdict[vertex]:
                self.gdict[ver].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self, vertex):
        # Start from the node
        # Visit and mark as visit
        # Add all unvisited neighbours to queue
        # Take vertex from the queue and repeat untill empty
        visited = set()
        visited.add(vertex)
        queue = [vertex]    # from collection import deque  deque([vertex])- for time efficiency when pop element
        while queue:
            vertex = queue.pop(0)       # vertext = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                for neighbours in self.gdict[vertex]:
                    if neighboursnot in visited:
                        queue.append(neighbours)

        return visited


    def bfs_search(self, vertex):
        # prefered method
        # Time O(V+E)
        # Space O(V)
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])    #  deque([vertex])- for time efficiency when pop element
        while queue:    # O(V)
            current_vertex = queue.popleft()
            for neighbours in self.gdict[current_vertex]:   # O(E)
                if neighbours not in visited:
                    visited.add(neighbours)
                    queue.append(neighbours)

        return visited

    def dfs_search(self, vertex):
        # Time O(V+E)
        # Space O(V)
        visited = set()
        order = []
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                order.append(current_vertex)
            for neighbour in self.gdict[current_vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
        return order


new_dict = {'a': ['b', 'c'], 'b': ['a', 'd'], 'c':['a'], 'd': ['b']}

graph = Graph(new_dict)
print(graph.gdict)
print(graph.dfs_search("a"))
print(graph.bfs_search("a"))
    