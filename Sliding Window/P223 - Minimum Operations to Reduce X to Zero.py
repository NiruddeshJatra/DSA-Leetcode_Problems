# Time Complexity:
# - O(N) where N is length of nums array
#   - Initial sum calculation: O(N)
#   - Single pass with sliding window: O(N)
#   - Each element is added and removed at most once

# Space Complexity:
# - O(1), using only primitive variables
#   - maxSubarrLen, currentSum, total, left, right
#   - No additional data structures

# INTUITION:
# Instead of directly finding elements to remove summing to x,
# we can find the longest subarray that sums to (total - x)
# This converts the problem to finding longest subarray with target sum
# Using sliding window because:
# - We want contiguous elements
# - We can easily maintain running sum
# - Can shrink/expand window based on current sum

# ALGO:
# 1. Calculate total sum of array
# 2. Use sliding window to find longest subarray with sum (total - x):
#    - Expand window by adding elements from right
#    - If sum > target, shrink window from left
#    - When sum == target, update max length
# 3. If no valid subarray found, return -1
# 4. Return (array length - max subarray length)

class Solution:
   def minOperations(self, nums: List[int], x: int) -> int:
       # Initialize variables
       maxSubarrLen, currentSum = -1, 0
       total = sum(nums)
       left = 0
       
       # Sliding window to find longest subarray with sum (total - x)
       for right in range(len(nums)):
           # Add current element to window
           currentSum += nums[right]
           
           # Shrink window if sum too large
           while left <= right and currentSum > total - x:
               currentSum -= nums[left]
               left += 1
               
           # Update max length if target sum found
           if currentSum == total - x:
               maxSubarrLen = max(maxSubarrLen, right - left + 1)
       
       # Return -1 if no solution found
       if maxSubarrLen == -1:
           return -1
           
       # Return minimum operations needed
       return len(nums) - maxSubarrLen
