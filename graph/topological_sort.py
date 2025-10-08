from collections import defaultdict


class Graph:
    def __init__(self, number_vertices):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topological_sort_util(self, vertex, visited, stack):
        visited.add(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)
        
        stack.append(vertex)

    def topological_sort(self):
        visited = set()
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)
        
        stack.reverse()
        return stack


# Time O(V + E)
# Space O(V)


g = Graph(4)
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

print(g.topological_sort())