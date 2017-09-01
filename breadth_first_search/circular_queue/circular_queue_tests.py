import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temp = Queue()
        temp.array[0] = 1
        temp.length = 1
        temp.back = 1
        cls.one = temp
        temp = Queue()
        temp.array[0] = 1
        temp.array[1] = 2
        temp.length = 1
        temp.front = 1
        temp.back = 2
        cls.dequeue = temp
        temp = Queue()
        temp.array[0] = 1
        temp.array[1] = 2
        temp.length = 2
        temp.back = 2
        cls.onetwo = temp

    def test00_interface(self):
        test_queue = empty_queue()
        test_queue.enqueue("foo")
        _ = test_queue.peek()
        _ = test_queue.dequeue()
        test_queue.size()
        test_queue.is_empty()
    
    def test_queue_repr(self):
        temp = "Queue([" + "None, " * 4999 + "None], 0, 0, 5000, 0)"
        self.assertEqual(str(empty_queue()), temp)

    def test_empty_queue(self):
        test = Queue()
        self.assertEqual(empty_queue(), test)

    def test_enqueue(self):
        test = Queue()
        test.enqueue(1)
        self.assertEqual(test, self.one)
        test.enqueue(2)
        self.assertEqual(test, self.onetwo)

    def test_enqeue_reset(self):
        test = Queue()
        for i in range(5000):
            test.enqueue(i)
        val = test.dequeue()
        test.enqueue(5001)
        temp = [None] * 5000
        for i in range(5000):
            temp[i] = i
        temp[0] = 5001
        self.assertEqual(test.array, temp)

    def test_enqueue_error(self):
        test = Queue()
        for i in range(5000):
            test.enqueue(i)
        self.assertRaises(IndexError, test.enqueue, 1)

    def test_dequeue_error(self):
        test = Queue()
        self.assertRaises(IndexError, test.dequeue)

    def test_dequeue(self):
        test = Queue()
        test.enqueue(1)
        test.enqueue(2)
        self.assertEqual(test.dequeue(), 1)

    def test_deqeue_reset(self):
        temp = [None] * 5000
        for i in range(5000):
            temp[i] = i
        test = Queue()
        for i in range(5000):
            test.enqueue(i)
        for i in range(4999):
            test.dequeue()
        for i in range(50):
            test.enqueue(i)
        for i in range(4):
            test.dequeue()
        self.assertEqual(test.array, temp)
        self.assertEqual(test.front, 3)

    def test_deqeue_reset_2(self):
        temp = [None] * 5000
        for i in range(5000):
            temp[i] = i
        test = Queue()
        for i in range(5000):
            test.enqueue(i)
        for i in range(5000):
            test.dequeue()
        for i in range(50):
            test.enqueue(i)
        for i in range(50):
            test.dequeue()
        self.assertEqual(test.array, temp)
        self.assertEqual(test.front, 50)

    def test_peek_reset(self):
        test = Queue()
        for i in range(5000):
            test.enqueue(i)
        for i in range(5000):
            test.dequeue()
        for i in range(50):
            test.enqueue(i)
        for i in range(50):
            test.dequeue()
        self.assertRaises(IndexError, test.peek)

    def test_peek_error(self):
        test = Queue()
        self.assertRaises(IndexError, test.peek)
    
    def test_peek(self):
        test = Queue()
        test.enqueue(1)
        test.enqueue(2)
        self.assertEqual(test.peek(), 1)
        test.dequeue()
        self.assertEqual(test.peek(), 2)

    def test_size(self):
        test = Queue()
        self.assertEqual(test.size(), 0)
        test.enqueue(1)
        self.assertEqual(test.size(), 1)
        test.enqueue(2)
        self.assertEqual(test.size(),2)

    def test_is_empty(self):
        test = Queue()
        self.assertEqual(test.is_empty(), True)
        test.enqueue(1)
        self.assertEqual(test.is_empty(), False)
 
if __name__ == "__main__":
    unittest.main()
