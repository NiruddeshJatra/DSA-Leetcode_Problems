# INTUITION (Beginner-Friendly Explanation):
# Imagine you are a robot trying to move from the top-left corner to the bottom-right corner of a grid.
# You can only move right or down. How many unique paths can you take to reach your goal?
# 
# HOW DOES THIS SOLUTION WORK?
# 1. **Initialization:** We create a 2D `dp` array where `dp[i][j]` will store the number of ways to reach cell `(i, j)`.
# 2. **Base Cases:** 
#    - First row (`dp[0][j]`) and first column (`dp[i][0]`) are filled with `1` since there’s only one way to move along the edges (straight line).
# 3. **Dynamic Programming:** For each cell, the number of ways to get there is the sum of ways to get to the cell above it (`dp[i-1][j]`) 
#    and the cell to its left (`dp[i][j-1]`).
# 4. **Result:** The value in the bottom-right cell `dp[m-1][n-1]` is the total number of unique paths.

# TIME COMPLEXITY:
# - O(m * n) → We fill each cell in the grid exactly once.
#
# SPACE COMPLEXITY:
# - O(m * n) → We store the results for all cells in a 2D array.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: Initialize the dp array with -1 (for clarity)
        dp = [[-1] * n for _ in range(m)]
        
        # Step 2: Fill the first row and first column with 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Step 3: Fill the dp table using the recursive relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Step 4: Return the result from the bottom-right cell
        return dp[m-1][n-1]
