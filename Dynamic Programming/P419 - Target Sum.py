
# Time Complexity:
# - O(N*S), where N is the length of the array and S is the sum of all elements.
# - The state space is limited by the number of elements and possible sums at each step.

# Space Complexity:
# - O(N*S) for the memoization dictionary in the recursive solution.
# - Can be optimized with an iterative bottom-up approach.

# INTUITION:
# This problem asks us to find the number of ways to assign "+" and "-" to elements to reach a target sum.
# This is equivalent to partitioning the array into two subsets where their difference equals target.
# 
# We can use dynamic programming with memoization to avoid recomputing overlapping subproblems.
# At each step, we have two choices: add the current number or subtract it from our running sum.
# 
# For example, with nums = [1,1,1,1,1] and target = 3:
# - We can try +1+1+1+1-1 = 3
# - Or +1+1+1-1+1 = 3
# - Or +1+1-1+1+1 = 3
# - Or +1-1+1+1+1 = 3
# - Or -1+1+1+1+1 = 3
# So there are 5 ways to reach the target.

# ALGO:
# 1. Define a recursive function f(i, k) that represents the number of ways to reach sum k using the first i elements.
# 2. Base case: If i < 0 (we've considered all elements), return 1 if k = 0, otherwise 0.
# 3. For each element, recursively explore both choices: adding and subtracting the current number.
# 4. Use memoization to store results of subproblems to avoid recomputation.
# 5. Return the final count of ways to reach the target sum.

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}  # Memoization dictionary for storing computed results
        
        def calculate(index, currentSum):
            # Base case: if we've considered all numbers
            if index < 0:
                return 1 if currentSum == 0 else 0
            
            # Check if we've already computed this state
            if (index, currentSum) in memo:
                return memo[(index, currentSum)]
            
            # Try both adding and subtracting the current number
            addNumber = calculate(index - 1, currentSum + nums[index])
            subtractNumber = calculate(index - 1, currentSum - nums[index])
            
            # Store the result in our memoization dictionary
            memo[(index, currentSum)] = addNumber + subtractNumber
            return memo[(index, currentSum)]
        
        # Start the recursion from the last index with the target sum
        return calculate(n - 1, target)
    
    # Iterative bottom-up solution (more efficient)
    def findTargetSumWays_iterative(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If target is outside the possible range or the sum is odd
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        # We need to find the number of ways to create a subset with sum = (total + target) / 2
        targetSum = (total + target) // 2
        
        # Initialize DP array
        dp = [0] * (targetSum + 1)
        dp[0] = 1  # Empty subset has sum 0
        
        # Fill the DP array
        for num in nums:
            for j in range(targetSum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[targetSum]

