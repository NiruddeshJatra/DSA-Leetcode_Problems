# Time Complexity: O(log(n - k) + k), where `n` is the length of `arr` and `k` is the number of closest elements to find.  
# - The binary search operates on a range of size `n - k`, taking O(log(n - k)).  
# - Extracting the final slice of `k` elements takes O(k).

# Space Complexity: O(k).  
# - The result list requires O(k) space to store the closest elements.

# INTUITION:  
# The goal is to find the `k` closest elements to `x` in a sorted array.  
# A **binary search** approach is used to efficiently locate the starting point of the `k` elements, leveraging the sorted nature of the array.  
# The key insight is to compare the distances of potential elements to `x` and adjust the search range accordingly.  
# Using a range `[left, right]` (of length `n - k`), the algorithm identifies the optimal starting index `left` where the `k` closest elements are located.  
# This approach is efficient because:  
# 1. Binary search quickly narrows down the potential range of indices.  
# 2. Extracting a slice from the array is direct and avoids additional comparisons.

# ALGORITHM:  
# 1. Initialize pointers:  
#    - `left` at the start of the array.  
#    - `right` at `len(arr) - k`, since `k` elements must fit in the range.  
# 2. Perform binary search:  
#    - Calculate the midpoint `mid`.  
#    - Compare the distances:  
#      - If `x - arr[mid] <= arr[mid + k] - x`, move `right` to `mid`.  
#      - Otherwise, move `left` to `mid + 1`.  
# 3. Once the loop ends, the starting index of the `k` closest elements is `left`.  
# 4. Return the slice of the array from `left` to `left + k`.

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize the binary search bounds
        leftPointer, rightPointer = 0, len(arr) - k

        # Perform binary search to locate the starting point
        while leftPointer < rightPointer:
            midPointer = (leftPointer + rightPointer) // 2

            # Compare distances to x and adjust bounds
            if x - arr[midPointer] <= arr[midPointer + k] - x:
                rightPointer = midPointer
            else:
                leftPointer = midPointer + 1

        # Return the k closest elements starting from the found index
        return arr[leftPointer:leftPointer + k]
