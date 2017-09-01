import unittest
from breadth_first_search import *

class TestBFS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vert = Vertex(1)
        cls.graph_one = Graph()
        cls.graph_one.add_edge(0, 1)
        cls.graph_one.add_edge(0, 2)
        cls.graph_one.add_edge(1, 2)
        cls.graph_one.add_edge(2, 0)
        cls.graph_one.add_edge(2, 3)
        cls.graph_one.add_edge(3, 3)

    def test_vertex_repr(self):
        self.assertEqual(str(self.vert), "Vertex(1, [])")

    def test_graph_repr_empty(self):
        temp = Graph()
        self.assertEqual(str(temp), "Graph(HashTable(" +
                "[[], [], [], [], [], [], [], []], 8, 0, 0))")

    def test_add_vertex(self):
        temp = Graph()
        temp.add_vertex(0)
        self.assertEqual(str(temp), "Graph(HashTable" +
        "([[(0, Vertex(0, []))], [], [], [], [], [], [], []], 8, 1, 0))")
        temp.add_vertex("hi")
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, []))," +
        " (104, Vertex('hi', []))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_add_edge_two_vertices(self):
        temp = Graph()
        temp.add_vertex(0)
        temp.add_vertex("hi")
        temp.add_edge(0, "hi")
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', []))], [], [], [], [], [], [], []], 8, 2, 1))") 
        temp.add_edge("hi", 0)
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', [0]))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_add_edge_two_vertices_cross_edge_true(self):
        temp = Graph()
        temp.add_vertex(0)
        temp.add_vertex("hi")
        temp.add_edge(0, "hi", cross_edge=True)
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', [0]))], [], [], [], [], [], [], []], 8, 2, 1))") 
        
    def test_add_edge_one_vertices(self):
        temp = Graph()
        temp.add_vertex(0)
        temp.add_edge(0, "hi")
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', []))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_add_edge_one_vertices_cross_edge_true(self):
        temp = Graph()
        temp.add_vertex(0)
        temp.add_edge(0, "hi", cross_edge=True)
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', [0]))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_add_edge_no_vertices(self):
        temp = Graph()
        temp.add_edge(0, "hi")
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', []))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_add_edge_no_vertices_cross_edge_true(self):
        temp = Graph()
        temp.add_edge(0, "hi", cross_edge=True)
        self.assertEqual(str(temp), "Graph(HashTable([[(0, Vertex(0, ['hi']))," +
        " (104, Vertex('hi', [0]))], [], [], [], [], [], [], []], 8, 2, 1))") 

    def test_get_key(self):
        self.assertEqual(get_key(1), 1)
        self.assertEqual(get_key("hi"), 104)

    def test_graph_one_0(self):
        self.assertEqual(self.graph_one.breadth_first_search(0), "0123") 
        
    def test_graph_one_1(self):
        self.graph_one.reset_visited(0)
        self.assertEqual(self.graph_one.breadth_first_search(1), "1203") 

    def test_graph_one_2(self):
        self.graph_one.reset_visited(1)
        self.assertEqual(self.graph_one.breadth_first_search(2), "2031") 

    def test_graph_one_3(self):
        self.graph_one.reset_visited(2)
        self.assertEqual(self.graph_one.breadth_first_search(3), "3")
    
if __name__ == '__main__':
    unittest.main()
