import unittest
from hash_table_chaining import *

class HashTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.empty = HashTable()
        one = empty_hash_table()
        one.ls[1] = [(1, "one")]
        one.length = 1
        cls.one = one
        two = empty_hash_table()
        two.ls[1] = [(1, "one"), (9, "two")]
        two.length = 2
        two.colls = 1
        cls.two = two
        full = empty_hash_table()
        for i in range(12):
            full = insert(full, i, "dog")
        cls.full = full
        full_rehash = empty_hash_table()
        for i in range(8):
            full_rehash = insert(full_rehash, i, "dog")
        for i in range(5):
            full_rehash.ls[i].append((i+8, "dog"))
        cls.full_rehash = full_rehash
        double = HashTable()
        double.ls = [[] for i in range(16)]
        double.cap = 16
        for i in range(13):
            double = insert(double, i, "dog")
        cls.double = double
    
    def test_repr(self):
        temp = HashTable()
        self.assertEqual(str(temp), "HashTable([[], [], [], [], [], [], [], []], 8, 0, 0)")

    def test_empty_hash_table(self):
        self.assertEqual(empty_hash_table(), self.empty)

    def test_insert(self):
        temp = empty_hash_table()
        self.assertEqual(insert(temp, 1, "one"), self.one)

    def test_insert_duplicates(self):
        temp = empty_hash_table()
        temp = insert(temp, 1, "no")
        self.assertEqual(insert(temp, 1, "one"), self.one)

    def test_insert_rehash(self):
        self.assertEqual(insert(self.full, 12, "dog"), self.double)

    def test_rehash(self):
        self.assertEqual(rehash(self.full_rehash), self.double)

    def test_get(self):
        self.assertEqual(get(self.one, 1), "one")
        self.assertEqual(get(self.two, 1), "one")
        self.assertEqual(get(self.two, 9), "two")

    def test_get_lookup_error(self):
        self.assertRaises(LookupError, get, self.empty, 1)
        self.assertRaises(LookupError, get, self.empty, 20)

    def test_remove(self):
        temp = empty_hash_table()
        temp = insert(temp, 1, "one")
        temp = insert(temp, 9, "two")
        self.assertEqual(remove(temp, 9), self.one)
        self.assertEqual(remove(temp, 1), self.empty)
    
    def test_remove_lookup_error(self):
        self.assertRaises(LookupError, remove, self.one, 2)
        self.assertRaises(LookupError, remove, self.one, 9)

    def test_size(self):
        self.assertEqual(size(self.empty), 0)
        self.assertEqual(size(self.one), 1)
        self.assertEqual(size(self.double), 13)

    def test_load_factor(self):
        self.assertEqual(load_factor(self.two), 0.25)

    def test_collisions(self):
        self.assertEqual(collisions(self.empty), 0)
        self.assertEqual(collisions(self.double), 0)
        self.assertEqual(collisions(self.two), 1)
        full = empty_hash_table()
        for i in range(12):
            full = insert(full, i, "dog")
        self.assertEqual(collisions(full), 4)

    def test_all(self):
        temp = empty_hash_table()
        temp = insert(temp, 1, "one")
        temp = insert(temp, 2, "two")
        self.assertEqual(temp.length, 2)
        temp = remove(temp, 2)
        self.assertEqual(temp.length, 1)
        temp = insert(temp, 9, "nine")
        self.assertEqual(temp.colls, 1)

if __name__ == '__main__':
    unittest.main()
