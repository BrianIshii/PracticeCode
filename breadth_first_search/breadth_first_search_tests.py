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
        self.assertEqual(str(temp), "Graph({}, 0)")

    def test_add_vertex(self):
        temp = Graph()
        temp.add_vertex(0)
        self.assertEqual(str(temp), "Graph({0: Vertex(0, [])}, 1)")
        temp.add_vertex("hi")
        self.assertEqual(str(temp), "Graph({0: Vertex(0, []), " +
                "4: Vertex('hi', [])}, 2)")

    def test_add_edge_two_vertices(self):
        pass

    def test_add_edge_one_vertices(self):
        pass

    def test_add_edge_no_vertices(self):
        pass

    def test_get_key(self):
        pass

    


"""
    def test_graph_one_0(self):
        self.assertEqual(self.graph_one.breadth_first_search(0), "0123") 
        
    def test_graph_one_1(self):
        self.assertEqual(self.graph_one.breadth_first_search(1), "1203") 

    def test_graph_one_2(self):
        self.assertEqual(self.graph_one.breadth_first_search(2), "2031") 

    def test_graph_one_3(self):
         self.assertEqual(self.graph_one.breadth_first_search(3), "3")
    
    def test_add_cross_true(self):
        temp = Graph()
        temp.add_edge(0, 1, cross_edge=True)
        self.assertEqual(temp.breadth_first_search(0), "01")
        self.assertEqual(temp.breadth_first_search(1), "10")
"""
if __name__ == '__main__':
    unittest.main()
