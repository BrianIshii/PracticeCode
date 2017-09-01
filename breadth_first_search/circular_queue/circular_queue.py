# an AnyValue is an element of any type
class Queue:
    def __init__(self):
        self.array = [None] * 5000
        self.front = 0
        self.back = 0
        self.capcity = 5000
        self.length = 0

    def __eq__(self, other):
        return (type(other) == Queue
                and self.array == other.array
                and self.front == other.front
                and self.back == other.back
                and self.capcity == other.capcity
                and self.length == other.length)
    
    def __repr__(self):
        return ("Queue({!r}, {!r}, {!r}, {!r}, {!r})".format(self.array,
            self.front, self.back, self.capcity, self.length))
    # Queue AnyValue ->            
    # adds the AnyValue to the end of the Queue
    def enqueue(self, val):
        if self.length == self.capcity:
            raise IndexError()
        else:
            if self.back == self.capcity:
                self.back = 0
            self.array[self.back] = val
            self.length += 1
            self.back += 1

    # Queue ->
    # returns the first element in the queue while removing it
    def dequeue(self):
        if self.length == 0:
            raise IndexError()
        else:
            if self.front == self.capcity:
                self.front = 0
            val = self.array[self.front]
            self.front += 1
            self.length -= 1
            return val

    # Queue ->
    # returns the first element in the queue
    def peek(self):
        if self.length == 0:
            raise IndexError()
        else:
            return self.array[self.front]
    # Queue ->
    # returns the length of the Queue
    def size(self):
        return self.length
    
    # Queue ->
    # Determines if the Queue is empty
    def is_empty(self):
        return self.length == 0
# -> Queue
# returns an empty Queue
def empty_queue():
    return Queue()
