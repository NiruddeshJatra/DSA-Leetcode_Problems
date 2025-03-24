# Time Complexity:
# - O(N³), where N is the length of the input array
# - We have three nested loops: 
#   - Outer two loops iterate through different subarray ranges
#   - Inner loop tries all possible last balloons to burst
# - Each state is computed once and stored in the DP table

# Space Complexity:
# - O(N²) to store the dynamic programming table
# - We create a 2D DP array of size (N+2) × (N+2)

# INTUITION:
# The problem involves finding the maximum coins you can collect by bursting balloons strategically
# Key insights:
# - Adding boundary 1's helps handle edge cases and simplifies calculation
# - We solve the problem backwards - deciding the LAST balloon to burst in each subproblem
# - When we burst a balloon, we multiply its value with the boundary balloons that remain
# Example:
# nums = [3,1,5,8]
# Optimal strategy might be:
# 1. Burst 1 (gives 3×1×5 = 15 coins)
# 2. Burst 5 (gives 3×5×8 = 120 coins)
# 3. Burst 3 (gives 1×3×8 = 24 coins)
# 4. Burst 8 (gives 1×8×1 = 8 coins)
# Total max coins: 15 + 120 + 24 + 8 = 167

# ALGO:
# 1. Add boundary 1's to the input array
# 2. Create a 2D DP table initialized with zeros
# 3. Iterate through different subarray lengths in reverse
# 4. For each subarray, try bursting each balloon last
# 5. Calculate coins by multiplying with boundary balloons
# 6. Store maximum coins for each subproblem
# 7. Return the result for the entire array

class Solution:
   def maxCoins(self, nums: List[int]) -> int:
       # Add boundary 1's to handle edge cases
       nums = [1] + nums + [1]
       n = len(nums) - 2
       
       # Create DP table to store maximum coins for each subproblem
       dp = [[0] * (n + 2) for _ in range(n + 2)]
       
       # Iterate through different subarray lengths in reverse
       for length in range(1, n + 1):
           for left in range(1, n - length + 2):
               right = left + length - 1
               
               # Try bursting each balloon last in this subarray
               for lastBalloon in range(left, right + 1):
                   coins = (
                       nums[left - 1] * nums[lastBalloon] * nums[right + 1] +
                       dp[left][lastBalloon - 1] + 
                       dp[lastBalloon + 1][right]
                   )
                   dp[left][right] = max(dp[left][right], coins)
       
       # Return maximum coins for the entire array
       return dp[1][n]
