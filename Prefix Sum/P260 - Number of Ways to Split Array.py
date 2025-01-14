# Time Complexity:
# - O(N) where N is the length of the array
# - O(N) for initial sum calculation and O(N) for the single pass through array

# Space Complexity:
# - O(1) as we only use a few variables regardless of input size
# - No additional data structures are needed

# INTUITION:
# The problem asks to count ways to split an array where left sum >= right sum.
# Key insights:
# 1. We can calculate the total sum first, then track left sum as we iterate
# 2. Right sum at any point can be derived from (total - leftSum)
# 3. No need to recalculate sums repeatedly - use running sum technique
# This avoids nested loops and gives us O(N) efficiency.

# ALGORITHM:
# 1. Calculate total sum of array
# 2. Iterate through array except last element (we need at least one element on right)
# 3. For each position:
#    - Add current element to leftSum
#    - Compare leftSum with remaining sum (total - leftSum)
#    - If leftSum is greater or equal, increment valid ways counter
# 4. Return total number of valid ways

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Calculate total sum once
        totalSum = sum(nums)
        
        # Track running sum and count of valid splits
        leftSum = 0
        validSplits = 0
        
        # Check each possible split position except last
        for i in range(len(nums) - 1):
            leftSum += nums[i]
            rightSum = totalSum - leftSum
            
            if leftSum >= rightSum:
                validSplits += 1
        
        return validSplits
