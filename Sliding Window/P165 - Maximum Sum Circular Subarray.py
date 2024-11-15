# Time Complexity: O(n), where n is the length of nums.  
# We iterate through the array once, performing constant-time calculations at each step.

# Space Complexity: O(1).  
# The algorithm uses a constant number of variables, making it space-efficient.

# INTUITION:
# This problem extends the classic maximum subarray problem (Kadane's Algorithm) to circular arrays.  
# In a circular array, the maximum subarray can either:
# 1. Be a standard subarray contained entirely within the array (handled by Kadane's algorithm).  
# 2. Wrap around the edges of the array, utilizing the circular nature.  
# To compute the wrapped maximum, we observe that:
# - Wrapping around means excluding the smallest (minimum) subarray sum from the total array sum.  

# The algorithm keeps track of both the maximum and minimum subarray sums while traversing the array.  
# The maximum of `maxSum` (non-wrapped case) and `total - minSum` (wrapped case) is the answer.  
# Special Case: If all numbers are negative, `total - minSum` becomes 0, which is invalid. Thus, we only consider `maxSum` in such cases.

# ALGO:
# 1. Initialize variables to track:
#    - `maxSum` and `maxSumEndingHere` for maximum subarray sum.
#    - `minSum` and `minSumEndingHere` for minimum subarray sum.
#    - `total` for the sum of the entire array.
# 2. For each element in nums:
#    - Update `maxSumEndingHere` as the larger of `maxSumEndingHere + num` or `num`.
#    - Update `maxSum` to the maximum of itself and `maxSumEndingHere`.
#    - Similarly, update `minSumEndingHere` and `minSum` for minimum subarray sums.
#    - Add the current number to `total`.
# 3. Compute the result:
#    - If `maxSum > 0`, return the maximum of `maxSum` and `total - minSum`.
#    - Otherwise, return `maxSum` (for all-negative arrays).

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSumEndingHere, minSumEndingHere, total = 0, 0, 0
        maxSum, minSum = nums[0], nums[0]
        for num in nums:
            maxSumEndingHere = max(maxSumEndingHere + num, num)
            maxSum = max(maxSum, maxSumEndingHere)
            minSumEndingHere = min(minSumEndingHere + num, num)
            minSum = min(minSum, minSumEndingHere)
            total += num

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
