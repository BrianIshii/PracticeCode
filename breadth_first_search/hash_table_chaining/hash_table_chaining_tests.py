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
            full.insert(i, "dog")
        cls.full = full
        full_rehash = empty_hash_table()
        for i in range(8):
            full_rehash.insert(i, "dog")
        for i in range(5):
            full_rehash.ls[i].append((i+8, "dog"))
        cls.full_rehash = full_rehash
        double = HashTable()
        double.ls = [[] for i in range(16)]
        double.cap = 16
        for i in range(13):
            double.insert(i, "dog")
        cls.double = double
    
    def test_repr(self):
        temp = HashTable()
        self.assertEqual(str(temp), "HashTable([[], [], [], [], [], [], [], []], 8, 0, 0)")

    def test_empty_hash_table(self):
        self.assertEqual(empty_hash_table(), self.empty)

    def test_insert(self):
        temp = empty_hash_table()
        temp.insert(1, "one")
        self.assertEqual(temp, self.one)

    def test_insert_duplicates(self):
        test = empty_hash_table()
        test.insert(1, "no")
        temp = empty_hash_table()
        temp.insert(1, "no")
        self.assertEqual(temp, test)
        temp.insert(1, "one")
        self.assertEqual(temp, self.one)

    def test_insert_rehash(self):
        full = HashTable()
        for i in range(12):
            full.insert(i, "dog")
        full.insert(12, "dog")
        self.assertEqual(full, self.double)

    def test_rehash(self):
        full_rehash = HashTable()
        for i in range(8):
            full_rehash.insert(i, "dog")
        for i in range(5):
            full_rehash.ls[i].append((i+8, "dog"))
        full_rehash.rehash()
        self.assertEqual(full_rehash, self.double)

    def test_get(self):
        self.assertEqual(self.one.get(1), "one")
        self.assertEqual(self.two.get(1), "one")
        self.assertEqual(self.two.get(9), "two")

    def test_get_lookup_error(self):
        temp = empty_hash_table()
        temp.insert(1, "one")
        self.assertRaises(LookupError, temp.get, 9)
        self.assertRaises(LookupError, self.empty.get, 1)
        self.assertRaises(LookupError, self.empty.get, 20)

    def test_remove(self):
        temp = empty_hash_table()
        temp.insert(1, "one")
        temp.insert(9, "two")
        temp.remove(9)
        self.assertEqual(temp, self.one)
        temp.remove(1)
        self.assertEqual(temp, self.empty)
    
    def test_remove_lookup_error(self):
        self.assertRaises(LookupError, self.one.remove, 2)
        self.assertRaises(LookupError, self.one.remove, 9)

    def test_size(self):
        self.assertEqual(self.empty.size(), 0)
        self.assertEqual(self.one.size(), 1)
        self.assertEqual(self.double.size(), 13)

    def test_load_factor(self):
        self.assertEqual(self.two.load_factor(), 0.25)

    def test_collisions(self):
        self.assertEqual(self.empty.collisions(), 0)
        self.assertEqual(self.double.collisions(), 0)
        self.assertEqual(self.two.collisions(), 1)
        full = empty_hash_table()
        for i in range(12):
            full.insert(i, "dog")
        temp = full.collisions()
        self.assertEqual(temp, 4)

    def test_all(self):
        temp = empty_hash_table()
        temp.insert(1, "one")
        temp.insert(2, "two")
        self.assertEqual(temp.length, 2)
        temp.remove(2)
        self.assertEqual(temp.length, 1)
        temp.insert(9, "nine")
        self.assertEqual(temp.colls, 1)

if __name__ == '__main__':
    unittest.main()
