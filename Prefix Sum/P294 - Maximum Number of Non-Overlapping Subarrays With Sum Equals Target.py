# Time Complexity:
# - O(N) where N is length of input array
# - We traverse array once, doing O(1) set operations at each step

# Space Complexity:
# - O(N) for the set storing cumulative sums
# - In worst case, all prefix sums are unique and stored

# INTUITION:
# Using prefix sum + set technique to find subarrays with target sum.
# When we find a valid subarray, we clear the set to ensure non-overlapping
# condition. This greedy approach gives the maximum number of non-overlapping
# subarrays possible.

# ALGO:
# 1. Initialize:
#    - Result counter for valid subarrays
#    - Current sum to track running sum
#    - Set to store prefix sums (initialize with 0)
# 2. For each number:
#    - Add to current sum
#    - Check if (currentSum - target) exists in set
#      * If yes: found valid subarray
#      * Clear set to prevent overlapping
#      * Increment result counter
#    - Add current sum to set
# 3. Return result counter

class Solution:
   def maxNonOverlapping(self, nums: List[int], target: int) -> int:
       # Track number of valid subarrays found
       validSubarrays = 0
       
       # Running sum of numbers processed so far
       prefixSum = 0
       
       # Set to store prefix sums, initialize with 0
       prefixSums = set([0])
       
       # Process each number
       for num in nums:
           # Update running sum
           prefixSum += num
           
           # Check if we can form subarray with target sum
           if prefixSum - target in prefixSums:
               # Found valid subarray
               # Clear set to ensure non-overlapping
               prefixSums = set()
               validSubarrays += 1
           
           # Add current prefix sum to set
           prefixSums.add(prefixSum)
       
       return validSubarrays
