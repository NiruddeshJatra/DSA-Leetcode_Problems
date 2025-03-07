# Time Complexity:
# - O(N), where N is the number of houses.
# - We pass through the list twice, solving the "House Robber" problem for two subarrays.

# Space Complexity:
# - O(1), as we use only a constant amount of extra space for the two variables.

# INTUITION:
# The problem is a variation of the classic "House Robber" problem, with the twist that the houses are arranged in a circle.
# If the first house is robbed, the last house cannot be robbed, and vice versa.
# Therefore, we break the problem into two subproblems:
# 1. Rob houses from index [1 to n-1] (excluding the first house).
# 2. Rob houses from index [0 to n-2] (excluding the last house).
# We take the maximum of these two results to get the optimal solution.

# Example:
# nums = [2, 3, 2]
# rob(nums[1:]) -> [3, 2] -> max profit = 3
# rob(nums[:-1]) -> [2, 3] -> max profit = 3
# Result = max(3, 3) = 3

# ALGO:
# 1. Handle the base case where there's only one house.
# 2. Define a helper function `simpleRob` to solve the linear house robber problem.
# 3. Calculate the maximum profit for two cases:
#    a. Rob from house 1 to n-1.
#    b. Rob from house 0 to n-2.
# 4. Return the maximum of the two results.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def simpleRob(nums):
            prev1, prev2 = 0, 0
            for num in nums:
                prev1, prev2 = max(prev1, prev2 + num), prev1
            return prev1

        if len(nums) == 1:
            return nums[0]
        return max(simpleRob(nums[1:]), simpleRob(nums[:-1]))
