# Time Complexity:
# - O(N), where N is length of nums array
#   - Each element is pushed and popped from deque at most once
#   - All deque operations (append, pop) are O(1)
# Space Complexity:
# - O(N) for the deque
#   - In worst case, deque could store all indices before any removal
# INTUITION:
# We use a monotonic queue approach with cumulative sums because:
# 1. Cumulative sums let us get any subarray sum in O(1) time using: sum(i,j) = prefix[j] - prefix[i]
# 2. Monotonic queue maintains a decreasing sequence of sums which gives us two benefits:
#    - Smaller sums that come later are useless (if larger sum wasn't valid, smaller won't be)
#    - Only need to check the front of queue for valid subarrays
# 3. Each element enters/exits queue at most once, giving O(N) complexity
# ALGO:
# 1. Initialize deque with [0,-1] for handling edge cases
# 2. For each position right in array:
#    - Add current number to running sum
#    - While sum difference with queue front ≥ k:
#      - Found valid subarray, update minLen
#      - Remove front of queue
#    - While queue not empty and current sum ≤ last sum in queue:
#      - Remove last element (maintaining decreasing order)
#    - Add current [sum, index] pair to queue
# 3. Return minLen if found valid subarray, else -1
from typing import List
import collections

class Solution:
   def shortestSubarray(self, nums: List[int], k: int) -> int:
       prefixSum = 0
       minLength = float('inf')
       # Store pairs of [prefixSum, index]
       monoQueue = collections.deque([[0, -1]])
       
       for i in range(len(nums)):
           prefixSum += nums[i]
           
           # Check if we can find valid subarrays
           while monoQueue and prefixSum - monoQueue[0][0] >= k:
               minLength = min(minLength, i - monoQueue.popleft()[1])
           
           # Maintain decreasing monotonic property
           while monoQueue and prefixSum <= monoQueue[-1][0]:
               monoQueue.pop()
               
           monoQueue.append([prefixSum, i])
       
       return -1 if minLength == float('inf') else minLength
