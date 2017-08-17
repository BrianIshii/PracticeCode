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
                
# -> Queue
# returns an empty Queue
def empty_queue():
    return Queue()

# Queue AnyValue -> Queue
# returns the Queue with the AnyValue added to the end of the Queue
def enqueue(q, val):
    if q.length == q.capcity:
        raise IndexError()
    else:
        if q.back == q.capcity:
            q.back = 0    
        q.array[q.back] = val
        q.length += 1
        q.back += 1
    return q

# Queue -> Tuple(AnyValue, Queue)
# returns a Tuple with be beginning value removed and the resulting Queue
def dequeue(q):
    if q.length == 0:
        raise IndexError()
    else:
        if q.front == q.capcity:
            q.front = 0
        val = q.array[q.front]
        q.front += 1
        q.length -= 1
    return (val, q)

# Queue -> AnyValue
# returns the element at the beginning of the Queue
def peek(q):
    if q.length == 0:
        raise IndexError()
    else:
        val = q.array[q.front]
    return val  

# Queue -> Int
# returns the number of elements in the queue
def size(q):
    return q.length

# Queue -> bool
# Determines whether the Queue is empty
def is_empty(q):
    return q.length == 0

