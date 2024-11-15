# Time Complexity: O(n), where n is the length of nums.  
# The algorithm traverses the array once, performing constant-time calculations per element.

# Space Complexity: O(1).  
# The algorithm uses a fixed number of variables, making it space-efficient.

# INTUITION:
# The problem is to find the maximum sum of a strictly ascending subarray.  
# By iterating through the array, we can identify ascending subarrays in real-time:
# - When the current element is greater than the previous one, it continues the ascending subarray.  
# - Otherwise, the subarray ends, and we reset the sum to start a new subarray.  
# At each step, we track the maximum sum encountered so far.  
# This approach avoids the need for nested loops, making it efficient.  

# ALGO:
# 1. Initialize `ans` to store the maximum sum and `windowSum` to track the sum of the current ascending subarray.
# 2. Start with the first element of `nums` as the initial sum.
# 3. Iterate through the array from the second element:
#    - If the current element is less than or equal to the previous one, reset `windowSum` to 0 (subarray breaks).
#    - Add the current element to `windowSum`.
#    - Update `ans` to the maximum of `ans` and `windowSum`.
# 4. Return `ans` as the result.

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = windowSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                windowSum = 0

            windowSum += nums[i]
            ans = max(ans, windowSum)

        return ans
