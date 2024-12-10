# Time Complexity: O(n), where n is the length of the input array `nums`.  
# - Calculating the prefix sum takes O(n).  
# - Iterating over `k` possible start positions and processing the subarrays takes O(n).  
# Hence, the overall complexity is O(n).

# Space Complexity: O(n), where n is the length of the input array `nums`.  
# - The `prefixSum` array stores cumulative sums for efficient range sum queries.  
# Thus, the space complexity is O(n).

# INTUITION:  
# The goal is to find the maximum sum of subarrays with a fixed length `k` from the input array `nums`.  
# By using a **prefix sum array**, we can efficiently calculate the sum of any subarray in constant time.  
# For subarrays that are `k` steps apart, we process subarrays starting from different initial offsets (from `0` to `k-1`).  
# This ensures that we evaluate all possible subarrays that respect the step size of `k`.  
# While iterating, we maintain the maximum sum encountered so far by using a running sum to track the largest subarray sum ending at each position.

# ALGO:  
# 1. Create a prefix sum array for `nums` to store cumulative sums.  
# 2. Initialize the result `ans` to negative infinity to track the maximum subarray sum.  
# 3. Iterate over each possible starting offset (`start`) in the range `[0, k-1]`:  
#    - For each offset, iterate through the subarrays with a step size of `k`.  
#    - Update the running sum for the current subarray and compare it to the global maximum (`ans`).  
#    - Reset the running sum if starting a new subarray gives a larger value.  
# 4. Return the maximum subarray sum (`ans`) after processing all offsets.

from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Build the prefix sum array
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        # Initialize the maximum sum as negative infinity
        ans = float('-inf')

        # Iterate through all possible starting offsets
        for start in range(k):
            currentSum = 0
            # Process subarrays with step size `k`
            for i in range(start, len(prefixSum) - k, k):
                subarraySum = prefixSum[i + k] - prefixSum[i]
                currentSum = max(subarraySum, currentSum + subarraySum)
                ans = max(ans, currentSum)

        return ans
