from collections import defaultdict
from circular_queue.circular_queue import *
from hash_table_chaining.hash_table_chaining import *

# a Graph is a defaultdict object
# an AnyValue is an element of any type

class Vertex:
    
    def __init__(self, value):
        self.value = value # an AnyValue
        self.edges = [] # a list
        self.visited = False # bool

    def __repr__(self):
        return "Vertex({!r}, {!r})".format(self.value, self.edges)

    def __eq__(self, other):
        return (type(other) == Vertex and
                self.value == other.value and
                self.edges == other.edges)

class Graph:

    def __init__(self):
        self.graph = HashTable() # a HashTable

    def __repr__(self):
        return "Graph({!r})".format(self.graph)

    # Graph AnyValue ->
    # adds a vertex object to the graph
    def add_vertex(self, value):
        self.graph.insert(get_key(value), Vertex(value))
    
    # Graph AnyValue AnyValue [bool] ->
    # adds an edge between two vertices
    def add_edge(self, k1, k2, cross_edge=False):
        v1 = self.is_vertex(k1)
        v2 = self.is_vertex(k2)
        if cross_edge is True:
            v2.edges.append(k1)
        v1.edges.append(k2)


 
    def breadth_first_search(self, start):
        if start not in self.graph:
            raise KeyError()
        traversal_order = ""

        queue = empty_queue()
        
        queue.enqueue(start)
        self.graph[start].visited = True

        while not is_empty(queue):
            vertex = queue.dequeue()
            traversal_order += str(vertex)
            for i in self.graph[vertex].edges:
                if self.graph[i].visited == False:
                    queue.enqueue(i)
                    self.graph[i].visited = True
        return traversal_order

    def is_vertex(self, value):
        try:
            return self.graph.get(get_key(value))
        except LookupError:
            self.add_vertex(value)
            return self.graph.get(get_key(value))

# AnyValue -> int
# returns the key for the value
def get_key(value):
    if type(value) is not int:
        value = ord(value[0])
    return value
