# INTUITION (For Beginners):
# Imagine you’re standing at the top of a grid, and you want to reach the bottom with the smallest possible sum.
# You can move straight down, diagonally left, or diagonally right.
# The goal is to compute the minimum sum of values you can collect along any valid falling path.

# HOW DOES THIS SOLUTION WORK?
# 1. **Initialization:** Start with the first row as the initial `dp` array.
# 2. **Iterate Through Rows:** For each cell in the current row:
#    - Add the current cell value to the minimum of the possible previous row values you can fall from:
#      - Directly above (`dp[j]`)
#      - Top-left (`dp[j-1]`, if within bounds)
#      - Top-right (`dp[j+1]`, if within bounds)
# 3. **Handle Edges:** Take care of boundary cases:
#    - Left edge → No top-left cell, so consider only the above and top-right cells.
#    - Right edge → No top-right cell, so consider only the above and top-left cells.
# 4. **Result:** The minimum value in the last updated `dp` array is the answer.

# TIME COMPLEXITY:
# - O(n²) → Iterate through all cells in the matrix.

# SPACE COMPLEXITY:
# - O(n) → Use a single array (`dp`) to store results for the previous row.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]  # Initialize dp with the first row

        # Iterate through the matrix row by row
        for i in range(1, n):
            temp = [0] * n  # Temporary array for the current row
            for j in range(n):
                # Calculate the minimum falling path sum for each cell
                if j == 0:
                    temp[j] = matrix[i][j] + min(dp[0], dp[1])
                elif j == n - 1:
                    temp[j] = matrix[i][j] + min(dp[-1], dp[-2])
                else:
                    temp[j] = matrix[i][j] + min(dp[j-1], dp[j], dp[j+1])

            dp = temp  # Update dp with the current row results

        return min(dp)  # Return the smallest value in the last row
