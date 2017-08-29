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
# -> HashTable
# returns an empty HashTable with an initial sie of 8
def empty_hash_table():
    return HashTable()

# HashTable Int Item -> HashTable
# returns a HashTable with the Item inserted
def insert(h, key, item):
    h_key = hash(key)
    index = h_key % h.cap
    length = len(h.ls[index])
    x = True
    if length > 0:
        h.colls += 1
        for i in range(len(h.ls[index])):
            k, it = h.ls[index][i]
            if key == k:
                h.ls[index][i] = (key, item)
                x = False
    if x is True:
        h.ls[index].append((key, item))
        h.length += 1
    if load_factor(h) > 1.5:
        h = rehash(h)
    return h

# HashTable -> HashTable
# returns a rehashed table with double the length
def rehash(h):
    length = h.cap * 2
    new_hash = HashTable()
    new_hash.ls = [[] for i in range(length)]
    new_hash.cap = h.cap * 2
    for i in range(h.cap):
        for j in range(len(h.ls[i])):
            key, item = h.ls[i][j]
            new_hash = insert(new_hash, key, item)
    return new_hash

# HashTable Int -> Item 
# returns the Item with the associated key from the HashTable
def get(h, key):
    index = hash(key) % h.cap
    if h.ls[index] == []:
        raise LookupError()
    else:
        for k, i in h.ls[index]:
            if key == k:
                return i

# HashTable Int -> HashTable
# returns the HashTable with the Item of the key removed
def remove(h, key):
    index = hash(key) % h.cap
    if h.ls[index] == []:
        raise LookupError()
    else:
        length = len(h.ls[index])
        for j in range(length):
            k, item = h.ls[index][j]
            if key == k:
                h.ls[index].remove(h.ls[index][j])
                h.length -= 1
                return h
        raise LookupError()

# HashTable -> Int
# returns the size of the HashTable
def size(h):
    return h.length

# HashTable -> Int
# returns the current load factor of the hash table
def load_factor(h):
    return (h.length / h.cap)

# HashTable -> Int
# returns the number of collisions that occured during insertions into the HashTable
def collisions(h):
    return h.colls