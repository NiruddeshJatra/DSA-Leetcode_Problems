# Time Complexity:
# - `__init__`: O(n * log(n)), where n is the length of `nums`.  
#   - Building the heap takes O(n), and removing excess elements down to size `k` takes O((n - k) * log(n)).
# - `add`: O(log(k)).  
#   - Each `heappush` or `heappop` operation takes O(log(k)) time since the heap size is limited to `k`.

# Space Complexity: O(k).  
# - The heap size is limited to `k`, so the space used is proportional to `k`.

# INTUITION:
# - The task is to design a class that efficiently tracks the k-th largest element in a dynamic stream of numbers.  
# - A **min-heap** of size `k` is ideal for this problem because it allows us to efficiently maintain the smallest of the top `k` largest elements at the root.  
# - The root of the heap will always represent the k-th largest element.

# ALGORITHM:
# 1. **Initialization (`__init__`)**:
#    - Store the given `nums` array as the initial heap and retain only the largest `k` elements using a min-heap.
#    - Use `heapify` to convert the list into a heap, and repeatedly pop elements until the heap size is `k`.
# 2. **Adding an Element (`add`)**:
#    - Add the new element to the heap using `heappush`.
#    - If the heap size exceeds `k`, remove the smallest element (heap root) using `heappop`.
#    - Return the root of the heap, which represents the k-th largest element.

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums  # Store all elements in a heap
        self.k = k
        heapq.heapify(self.minHeap)  # Convert to a min-heap
        
        # Maintain the heap size to be exactly `k`
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.minHeap, val)
        # If the heap size exceeds `k`, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the root of the heap, the k-th largest element
        return self.minHeap[0]

# Example Usage:
# Input:
# k = 3
# nums = [4, 5, 8, 2]
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(3))  # Output: 4
# print(kthLargest.add(5))  # Output: 5
# print(kthLargest.add(10)) # Output: 5
# print(kthLargest.add(9))  # Output: 8
# print(kthLargest.add(4))  # Output: 8
