# Time Complexity: O(n * log(3)) ≈ O(n), where n is the number of unique elements in `nums`.  
# - Converting `nums` to a set takes O(n) to remove duplicates.  
# - For each unique number, a `heappush` and potentially a `heappop` operation are performed, both of which take O(log(3)) as the heap size is limited to 3.  
# - Therefore, the overall complexity is approximately O(n).

# Space Complexity: O(3) ≈ O(1).  
# - The size of the heap is at most 3, so the space used by the heap is constant.  
# - Additionally, storing the unique elements of `nums` as a set also takes O(n) space.

# INTUITION:  
# The task is to find the third maximum element in the array. If there are fewer than three distinct elements, return the maximum element.  
# - To efficiently track the top three largest unique elements, we use a min-heap of size 3.  
# - A min-heap allows us to efficiently maintain the smallest of the top three largest elements at the root.  
# - As we iterate through the unique elements of the array, we add each element to the heap.  
# - If the heap size exceeds 3, we remove the smallest element (heap root).  
# - At the end, the root of the heap will be the third maximum element, provided the heap contains 3 elements.  
# - If there are fewer than 3 unique elements, the largest element is returned instead.

# ALGORITHM:  
# 1. Remove duplicates from `nums` by converting it to a set.  
# 2. If the number of unique elements is less than 3, return the maximum element.  
# 3. Initialize an empty min-heap.  
# 4. Iterate through the unique elements of `nums`:  
#    - Push the current element into the heap.  
#    - If the heap size exceeds 3, remove the smallest element (heap root).  
# 5. Return the root of the heap, which will be the third maximum element.

import heapq
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates
        nums = list(set(nums))
        minHeap = []

        # If fewer than 3 distinct elements, return the maximum
        if len(nums) < 3:
            return max(nums)

        # Maintain a min-heap of size 3
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > 3:
                heapq.heappop(minHeap)

        # The root of the heap is the third maximum
        return minHeap[0]

# Example Usage:
# Input: nums = [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.

# Input: nums = [1, 2]
# Output: 2
# Explanation: There are only two distinct elements, so the maximum (2) is returned.
