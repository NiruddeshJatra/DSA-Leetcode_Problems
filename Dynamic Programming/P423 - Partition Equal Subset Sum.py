# Time Complexity:
# - O(N*S), where N is the number of elements in the array and S is the sum of all elements divided by 2.
# - We have N elements and for each element, we consider targets from S down to the element's value.

# Space Complexity:
# - O(S) since we only need to keep track of targets from 0 to S.
# - We use a dictionary/defaultdict to store possible sums.

# INTUITION:
# This problem asks if we can partition the array into two subsets with equal sums.
# If we find a subset that sums to exactly half of the total sum, then the remaining elements
# must form a subset with the same sum.
#
# This is a variation of the classic "Subset Sum" problem, which can be solved using dynamic programming.
# Since we need to find if a subset sums to exactly half the total, we can:
# 1. Check if the total sum is odd (if yes, return false as we can't split evenly)
# 2. Set target = sum/2 and find if any subset sums to target
#
# For example, with array [1,5,11,5]:
# - Total sum = 22, so we need to find a subset that sums to 11
# - We can find the subset [1,5,5] which sums to 11
# - Therefore, we can partition the array into two equal sum subsets

# ALGO:
# 1. Check if the total sum is odd - if so, return False immediately.
# 2. Calculate the target sum (half of the total).
# 3. Use dynamic programming to find if any subset sums to the target:
#    - Use a boolean array/dictionary where dp[j] = True if we can form a sum j.
#    - Start with dp[0] = True (empty subset has sum 0).
#    - For each number in the array, update the dp table from right to left.
# 4. Return dp[target] which indicates if we can form a subset with sum equal to target.

from typing import List
from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # If sum is odd, we cannot partition into equal subsets
        if totalSum % 2 != 0:
            return False
        
        targetSum = totalSum // 2
        possibleSums = defaultdict(bool)
        possibleSums[0] = True  # Empty subset can form sum 0
        
        # For each number, update the possible sums we can create
        for num in nums:
            # Iterate backwards to avoid counting the same number multiple times
            for currentSum in range(targetSum, num - 1, -1):
                # If we could already make sum (currentSum - num), then we can make currentSum by adding num
                possibleSums[currentSum] |= possibleSums[currentSum - num]
        
        return possibleSums[targetSum]
    
    # Alternative implementation using a list instead of dictionary
    def canPartition_list(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # If sum is odd, we cannot partition into equal subsets
        if totalSum % 2 != 0:
            return False
            
        targetSum = totalSum // 2
        dp = [False] * (targetSum + 1)
        dp[0] = True  # Empty subset can form sum 0
        
        for num in nums:
            for j in range(targetSum, num - 1, -1):
                dp[j] |= dp[j - num]
                
        return dp[targetSum]
