from collections import defaultdict
from circular_queue.circular_queue import *
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

        queue = empty_queue()
        
        enqueue(queue, start)
        visited[start] = True

        while not is_empty(queue):
            edge, queue = dequeue(queue)
            traversal_order += str(edge)
            for i in self.graph[edge]:
                if visited[i] == False:
                    enqueue(queue, i)
                    visited[i] = True
        return traversal_order

