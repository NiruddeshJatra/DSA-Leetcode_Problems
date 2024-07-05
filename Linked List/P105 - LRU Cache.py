"""
### Problem
Implement an LRU (Least Recently Used) Cache that has `get` and `put` methods. It should be able to return the value of the key if the key exists in the cache and update or add the key if it is not present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

### Intuition
An LRU Cache can be efficiently implemented using a combination of a dictionary and a doubly linked list. The dictionary allows for O(1) access to cache items, while the doubly linked list maintains the order of usage, allowing O(1) updates for recently used items and O(1) removals for least recently used items.

### Approach
1. **Node Class**:
   - Define a `Node` class to represent each element in the doubly linked list.
   - Each node has a key, data, a previous pointer, and a next pointer.

2. **LRUCache Class**:
   - **Initialization**:
     - Use a dictionary (`self.cache`) to store key-node pairs.
     - Maintain a fixed capacity for the cache.
     - Initialize dummy head and tail nodes to simplify edge cases.
   - **Insert Method**:
     - Add a node right after the head to mark it as recently used.
   - **Delete Method**:
     - Remove a node from the doubly linked list.
   - **Get Method**:
     - Check if the key exists in the cache.
     - If it does, move the node to the head and return its value.
     - If not, return -1.
   - **Put Method**:
     - Add or update a key-value pair.
     - If the cache exceeds capacity, remove the least recently used node (right before the tail).

### Time Complexity
O(1) for both `get` and `put` operations since dictionary operations and linked list updates are constant time.

### Space Complexity
O(capacity), where capacity is the maximum number of elements the cache can hold.

### Code
"""

class Node:
    def __init__(self, key=None, data=None, prev=None, next=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key]
            self.delete(temp)
            self.insert(temp)
            return temp.data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.delete(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
