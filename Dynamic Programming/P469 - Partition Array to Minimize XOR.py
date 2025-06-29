# Time Complexity:
# - O(N^2 * K), where N is the length of nums and K is the number of parts.
# - We have N*K states in the DP, and for each state we iterate through up to N positions.

# Space Complexity:
# - O(N * K), for the memoization cache storing results for each (index, parts) state.

# INTUITION:
# We need to partition the array into exactly K non-empty subarrays such that the maximum XOR among all subarrays is minimized.
# This is a classic "minimize the maximum" problem that can be solved using dynamic programming.
# 
# The key insight is that for each position, we try all possible ways to end the current subarray and start a new one.
# We use memoization to avoid recomputing the same subproblems. For each state (current index, remaining parts),
# we try extending the current subarray to different ending positions and recursively solve for the remaining parts.
# We take the minimum over all possible maximum values.

# ALGO:
# 1. Define dp(index, parts) = minimum possible maximum XOR when partitioning nums[index:] into exactly 'parts' subarrays
# 2. Base cases:
#    - If parts == 0 and index == n: we've used all elements with exactly K parts, return 0
#    - If parts == 0 or index == n: invalid state, return infinity
# 3. For each state, try all possible ending positions for the current subarray:
#    - Calculate XOR of current subarray from index to i
#    - Recursively solve for remaining elements with (parts-1) subarrays
#    - Take maximum of current subarray XOR and recursive result
#    - Track minimum over all possible splits
# 4. Return dp(0, k) - minimum maximum XOR when partitioning entire array into K parts

from typing import List
from functools import cache

class Solution:
   def minXor(self, nums: List[int], k: int) -> int:
       numElements = len(nums)
       
       @cache
       def findMinMaxXor(currentIndex, remainingParts):
           # Base case: used all elements with exactly k parts
           if remainingParts == 0 and currentIndex == numElements:
               return 0
           # Invalid cases: no parts left but elements remain, or no elements but parts remain
           if remainingParts == 0 or currentIndex == numElements:
               return float('inf')

           currentSubarrayXor = 0
           minMaxXor = float('inf')

           # Try all possible ending positions for current subarray
           # Ensure we leave enough elements for remaining parts
           maxEndingPos = numElements - (remainingParts - 1)
           for endingPos in range(currentIndex, maxEndingPos):
               currentSubarrayXor ^= nums[endingPos]
               
               # Recursively solve for remaining parts
               nextResult = findMinMaxXor(endingPos + 1, remainingParts - 1)
               
               # Maximum XOR among current subarray and remaining optimal partition
               maxXorInThisPartition = max(currentSubarrayXor, nextResult)
               
               # Track minimum over all possible partitions
               minMaxXor = min(minMaxXor, maxXorInThisPartition)
               
           return minMaxXor
       
       return findMinMaxXor(0, k)
