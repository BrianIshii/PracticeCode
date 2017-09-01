class HashTable:
    def __init__(self):
        self.ls = [[] for i in range(8)]
        self.cap = 8
        self.length = 0
        self.colls = 0

    def __repr__(self):
        return "HashTable({!r}, {!r}, {!r}, {!r})".format(self.ls, self.cap,
                                                self.length, self.colls)

    def __eq__(self, other):
        return (type(other) == HashTable
                and self.ls == other.ls
                and self.cap == other.cap)
    
    # HashTable Int Item ->
    # inserts the Item into the HashTable
    def insert(self, key, item):
        h_key = hash(key)
        index = h_key % self.cap
        length = len(self.ls[index])
        x = True
        if length > 0:
            self.colls += 1
            for i in range(length):
                k, it = self.ls[index][i]
                if key == k:
                    self.ls[index][i] = (key, item)
                    x = False
        if x is True:
            self.ls[index].append((key, item))
            self.length += 1
        if self.load_factor() > 1.5:
            self.rehash()

    # HashTable ->
    # rehashes the table with double the length
    def rehash(self):
        length = self.cap * 2 
        self.colls = 0
        temp = HashTable()
        temp.ls = [[] for i in range(length)]
        temp.cap = length
        for i in range(self.cap):
            for j in range(len(self.ls[i])):
                key, item = self.ls[i][j]
                temp.insert(key, item)
        self.ls = temp.ls
        self.cap = length
    
    # HashTable Int -> Item 
    # returns the Item with the associated key from the HashTable
    def get(self, key):
        index = hash(key) % self.cap
        if self.ls[index] == []:
            raise LookupError()
        else:
            for k, i in self.ls[index]:
                if key == k:
                    return i   
    # HashTable Int -> HashTable
    # returns the HashTable with the Item of the key removed
    def remove(self, key):
        index = hash(key) % self.cap
        if self.ls[index] == []:
            raise LookupError()
        else:
            for j in range(len(self.ls[index])):
                k, item = self.ls[index][j]
                if key == k:
                    self.ls[index].remove(self.ls[index][j])
                    self.length -= 1
                    return
            raise LookupError()
    # HashTable -> Int
    # returns the size of the HashTable
    def size(self):
        return self.length

    # HashTable -> Int
    # returns the current load factor of the hash table
    def load_factor(self):
        return (self.length / self.cap)

    # HashTable -> Int
    # returns the number of collisions that occured during insertions into the HashTable
    def collisions(self):
        return self.colls

# -> HashTable
# returns an empty HashTable with an initial sie of 8
def empty_hash_table():
    return HashTable()
