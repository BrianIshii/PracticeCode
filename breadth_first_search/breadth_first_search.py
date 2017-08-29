from collections import defaultdict
from circular_queue.circular_queue import *
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
        self.graph = {} # a dictionay
        self.vertex_count = 0 # an int
        self.hash_table_size = 100 # an int

    def __repr__(self):
        return "Graph({!r}, {!r})".format(self.graph, self.vertex_count)

    # Graph AnyValue ->
    # adds a vertex object to the graph
    def add_vertex(self, value):
        self.graph[get_key(self.hash_table_size, value)] = Vertex(value)
        self.vertex_count += 1
    
    # Graph AnyValue AnyValue [bool]
    def add_edge(self, v1, v2, cross_edge=False):
        key1 = self.is_vertex(v1)
        key2 = self.is_vertex(v2)
        if cross_edge is True:
            self.graph[key2].edges.append(v1)
        self.graph[key1].edges.append(v2)


 
    def breadth_first_search(self, start):
        if start not in self.graph:
            raise KeyError()
        traversal_order = ""

        queue = empty_queue()
        
        enqueue(queue, start)
        self.graph[start].visited = True

        while not is_empty(queue):
            vertex, queue = dequeue(queue)
            traversal_order += str(vertex)
            for i in self.graph[vertex].edges:
                if self.graph[i].visited == False:
                    enqueue(queue, i)
                    self.graph[i].visited = True
        return traversal_order

    def is_vertex(self, value):
        if value not in self.graph:
            self.add_vertex(value)
        return get_key(self.hash_table_size, value)

# AnyValue -> int
# returns the key for the value
def get_key(hash_table_size, value):
    if type(value) is not int:
        value = ord(value[0])
    return value % hash_table_size
