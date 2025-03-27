# Time Complexity:
# - get(): O(1)
# - put(): O(1)
# All operations happen in constant time due to hash map and doubly linked list

# Space Complexity:
# - O(capacity), where capacity is the maximum number of key-value pairs

# INTUITION:
# Least Frequently Used (LFU) Cache Implementation
# Key challenges:
# - Track frequency of key access
# - Evict least frequently used items when cache is full
# - If multiple items have same frequency, evict least recently used

# Core Data Structures:
# 1. cache: Stores key-value pairs
# 2. countMap: Tracks frequency of each key
# 3. listMap: Stores keys grouped by their access frequency
# 4. Custom Doubly Linked List to manage order of items with same frequency

# ALGO:
# 1. When putting a new item:
#    - If cache is full, remove least frequently used item
#    - Add new item with frequency 1
# 2. When getting an item:
#    - Increment its frequency
#    - Move to appropriate frequency list
# 3. Use doubly linked list to maintain order within frequency groups

class Node:
   def __init__(self, val, prev=None, next=None):
       self.val = val      # Stores the key
       self.prev = prev    # Previous node in list
       self.next = next    # Next node in list

class LinkedList:
   def __init__(self):
       # Dummy nodes for easier list manipulation
       self.left = Node(0)   # Head of the list
       self.right = Node(0, self.left)  # Tail of the list
       self.left.next = self.right
       self.map = {}  # Tracks nodes by their value (key)

   def pushRight(self, val):
       # Add new node to the right side of the list
       node = Node(val, self.right.prev, self.right)
       self.map[val] = node
       self.right.prev = node
       node.prev.next = node

   def pop(self, val):
       # Remove a specific node from the list
       if val in self.map:
           node = self.map[val]
           node.next.prev, node.prev.next = node.prev, node.next
           self.map.pop(val, None)

   def popleft(self):
       # Remove and return the leftmost (least recently used) item
       res = self.left.next.val
       self.pop(res)
       return res

   def update(self, val):
       # Move a node to the right (most recently used position)
       self.pop(val)
       self.pushRight(val)

   def length(self):
       # Return number of items in the list
       return len(self.map)

class LFUCache:
   def __init__(self, capacity: int):
       self.cache = {}  # Main key-value storage
       self.capacity = capacity  # Maximum cache size
       self.lfuCnt = 0  # Least frequent use count
       self.countMap = defaultdict(int)  # Tracks frequency of each key
       self.listMap = defaultdict(LinkedList)  # Stores keys by their frequency

   def counter(self, key):
       # Increment frequency of a key
       cnt = self.countMap[key]
       self.countMap[key] += 1
       
       # Move key from current frequency list to next
       self.listMap[cnt].pop(key)
       self.listMap[cnt+1].pushRight(key)

       # Update least frequent use count if needed
       if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
           self.lfuCnt += 1

   def get(self, key: int) -> int:
       # Retrieve value and update its frequency
       if key in self.cache:
           self.counter(key)
           return self.cache[key]
       return -1

   def put(self, key: int, value: int) -> None:
       # Handle edge case of zero capacity
       if self.capacity == 0:
           return

       # Evict least frequently used item if cache is full
       if key not in self.cache and len(self.cache) == self.capacity:
           res = self.listMap[self.lfuCnt].popleft()
           self.cache.pop(res)
           self.countMap.pop(res)

       # Add or update key
       self.cache[key] = value
       self.counter(key)
       self.lfuCnt = min(self.lfuCnt, self.countMap[key])
