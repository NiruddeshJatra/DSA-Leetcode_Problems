# Time Complexity: O(n * log(k)), where n is the length of `nums` and k is the input value.  
# - For each element in `nums`, we perform a `heappush` and potentially a `heappop` operation on the heap, both of which take O(log(k)).  
# - Since there are n elements in `nums`, the total complexity is O(n * log(k)).

# Space Complexity: O(k).  
# - The size of the heap is at most k, so it uses O(k) space.

# INTUITION:  
# The goal is to find the k-th largest element in the array. Instead of sorting the entire array,  
# which would take O(n * log(n)), we can use a min-heap of size k to keep track of the k largest elements.  
# - A min-heap allows us to efficiently maintain the smallest element among the k largest elements at the root.  
# - As we iterate through the array, we add each element to the heap.  
# - If the heap size exceeds k, we remove the smallest element to ensure that only the k largest elements remain in the heap.  
# - At the end, the root of the heap will be the k-th largest element, as it is the smallest among the k largest elements.

# ALGORITHM:  
# 1. Initialize an empty min-heap.  
# 2. Iterate through all elements of `nums`:  
#    - Push the current element into the heap.  
#    - If the heap size exceeds k, remove the smallest element (heap root).  
# 3. Return the root of the heap, which will be the k-th largest element.

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        # Build a heap of size k
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # The root of the heap is the k-th largest element
        return minHeap[0]

# Example Usage:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
# Explanation: The 2nd largest element is 5.
