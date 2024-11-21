# Time Complexity:  
# - `set`: O(1), as appending to a list is an O(1) operation.  
# - `get`: O(log(n)), where `n` is the number of entries for the given `key`.  
#   - Binary search is used to find the largest timestamp ≤ the given `timestamp`.  

# Space Complexity: O(n), where `n` is the total number of key-value pairs stored in the `TimeMap`.  
# - The `hashmap` stores a list of (value, timestamp) pairs for each `key`.

# INTUITION:  
# The task is to implement a time-based key-value store that supports setting a value with a timestamp and retrieving the value for a given key at or before a certain timestamp.  
# - For efficient retrieval, the values for each key are stored in a sorted list of (value, timestamp) pairs.  
# - Binary search is used to quickly find the most recent value with a timestamp ≤ the given timestamp.  
# - This ensures that the `get` operation is fast even as the number of entries grows.

# ALGORITHM:  
# 1. **Initialization (`__init__`)**:  
#    - Create a `hashmap` where each key maps to a list of (value, timestamp) pairs.  
# 2. **Set Operation (`set`)**:  
#    - Append the (value, timestamp) pair to the list for the given `key`.  
# 3. **Get Operation (`get`)**:  
#    - Retrieve the list of (value, timestamp) pairs for the given `key`.  
#    - Use binary search to find the largest timestamp ≤ the given `timestamp`.  
#    - If no such timestamp exists, return an empty string. Otherwise, return the corresponding value.

from collections import defaultdict
from typing import List

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Store the (value, timestamp) pair for the key
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve the list of (value, timestamp) pairs for the key
        possibleValues = self.hashmap[key]
        left, right = 0, len(possibleValues)

        # Binary search to find the largest timestamp <= the given timestamp
        while left < right:
            mid = (left + right) // 2
            if possibleValues[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If no valid timestamp exists, return an empty string
        return "" if right == 0 else possibleValues[right - 1][0]


# Example Usage:
# obj = TimeMap()
# obj.set("key1", "value1", 1)
# print(obj.get("key1", 1))  # Output: "value1"
# print(obj.get("key1", 3))  # Output: "value1"
