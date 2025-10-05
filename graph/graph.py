# A defaultdict automatically creates a default value for any key that doesn’t exist.

# from collections import defaultdict

# graph = defaultdict(list)


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


new_dict = {'a': ['b', 'c'], 'b': ['d']}

graph = Graph(new_dict)
print(graph.gdict)
    