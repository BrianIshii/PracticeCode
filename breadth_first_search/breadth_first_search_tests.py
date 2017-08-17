import unittest
from breadth_first_search import *

class TestBFS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph_one = Graph()
        cls.graph_one.add_edge(0, 1)
        cls.graph_one.add_edge(0, 2)
        cls.graph_one.add_edge(1, 2)
        cls.graph_one.add_edge(2, 0)
        cls.graph_one.add_edge(2, 3)
        cls.graph_one.add_edge(3, 3)

    def test_graph_one(self):
        self.assertEqual(self.graph_one.breadth_first_search(2), "2031") 
        print(self.graph_one)

if __name__ == '__main__':
    unittest.main()
