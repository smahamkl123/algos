class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node mapping
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _insert(self, node):
        #insert the node at the stat, next to head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        #emove the node fom linked list and reattach the prev & next nodes
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        # check the hashmap and return, and remove the node from current position and move it to the start
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        #check the total elements in cache and remove the last node if it exceeds the capacity
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._insert(node)
        self.cache[key] = node

        if len(self.cache.keys()) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
            