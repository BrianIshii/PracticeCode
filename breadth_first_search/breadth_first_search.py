from collections import defaultdict

# a Graph is a defaultdict object

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def __repr__(self):
        return "Graph({!r})".format(self.graph)

    def add_edge(self, edge1, edge2):
        self.graph[edge1].append(edge2)

    def breadth_first_search(self, start):
        traversal_order = ""
        visited = [False]*(len(self.graph))

        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            edge = queue.pop(0)
            traversal_order += str(edge)
            for i in self.graph[edge]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return traversal_order

