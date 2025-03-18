# Time Complexity:
# - O(M * N), where M is the number of rows and N is the number of columns in the matrix.
# - We iterate through each cell of the matrix exactly once.

# Space Complexity:
# - O(M * N) for the dp array, which is one row and column larger than the input matrix.

# INTUITION:
# To find the maximal square of 1's, we use dynamic programming. The key insight is that if a cell contains a '1',
# the largest square ending at that cell depends on the squares ending at its left, top, and top-left neighbors.
# By taking the minimum of these three adjacent cells in our dp array and adding 1, we get the side length of the 
# largest square ending at the current cell.
#
# Example:
# Consider a matrix:
# [
#   ["1","0","1","1","0"],
#   ["1","1","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
#
# If we're at position (2,3) (0-indexed) with a '1', we look at:
# - Top: dp[1][3] = 2
# - Left: dp[2][2] = 2
# - Top-left: dp[1][2] = 2
# Min of these is 2, so dp[2][3] = 2+1 = 3, meaning a 3x3 square ends here.

# ALGO:
# 1. Initialize a dp array with one extra row and column (all filled with 0's).
# 2. For each cell in the matrix:
#    a. If the cell contains a '1', calculate dp[i+1][j+1] as min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1.
#    b. Update the maximum side length found so far.
# 3. Return the area of the largest square (maxSide^2).

class Solution:
   def maximalSquare(self, matrix: List[List[str]]) -> int:
       if not matrix or not matrix[0]:
           return 0
           
       rows, cols = len(matrix), len(matrix[0])
       dp = [[0] * (cols + 1) for _ in range(rows + 1)]
       maxSideLength = 0

       for i in range(rows):
           for j in range(cols):
               if matrix[i][j] == '1':
                   # The value at dp[i+1][j+1] represents the side length of the largest square 
                   # whose bottom right corner is at position (i,j) in the original matrix
                   dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                   maxSideLength = max(maxSideLength, dp[i+1][j+1])

       # Return the area of the largest square
       return maxSideLength * maxSideLength
