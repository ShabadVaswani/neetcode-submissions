class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict()
        self.left  = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.ru = None
        self.cap = capacity
        self.length = 0

    def remove(self, node):
        nxt, prv = node.next, node.prev
        prv.next = nxt
        nxt.prev = prv

    def add(self, node):
        temp = self.right.prev 
        temp.next = node
        node.prev = temp
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.put(key, self.cache[key].val) 
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
            self.length+=1

        if self.cap < self.length:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
            self.length-=1
        
