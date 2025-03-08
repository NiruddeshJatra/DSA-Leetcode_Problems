# INTUITION (Beginner-Friendly Explanation):
# Imagine you're a robot trying to move through a grid, but this time some cells are blocked (obstacles).
# You can only move right or down, and you can't pass through cells with obstacles.
# The goal is to find how many unique ways you can reach the bottom-right corner from the top-left corner.
#
# HOW DOES THIS SOLUTION WORK?
# 1. **Initial Check:** If the starting or ending cell is an obstacle, return `0` immediately — no path exists.
# 2. **DP Array Setup:** Create a 2D `dp` array where `dp[i][j]` will store the number of unique paths to cell `(i, j)`.
# 3. **Initialize the First Row & Column:** 
#    - Fill with `1` until you hit an obstacle (`1`). After that, all cells in that row or column become unreachable.
# 4. **Fill the DP Table:** For each cell:
#    - If it’s not an obstacle, paths to `dp[i][j]` are the sum of paths from the top (`dp[i-1][j]`) and left (`dp[i][j-1]`).
#    - If it’s an obstacle, set `dp[i][j]` to `0`.
# 5. **Result:** The value in the bottom-right cell `dp[m-1][n-1]` is the total number of unique paths.

# TIME COMPLEXITY:
# - O(m * n) → Fill each cell exactly once.
#
# SPACE COMPLEXITY:
# - O(m * n) → Use a 2D array to store the number of ways for each cell.

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Step 1: Handle the edge case where the start or end is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Step 2: Initialize the first column
        for i in range(m):
            if grid[i][0] != 1:
                dp[i][0] = 1
            else:
                break  # Stop if an obstacle is encountered

        # Step 3: Initialize the first row
        for j in range(n):
            if grid[0][j] != 1:
                dp[0][j] = 1
            else:
                break  # Stop if an obstacle is encountered
        
        # Step 4: Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] != 1:  # Only calculate if there's no obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Step 5: Return the result
        return dp[m-1][n-1]
