# Time Complexity:
# - O(M*N), where M is the number of rows and N is the number of columns
# - We iterate through each cell in the matrix exactly once
# - Each cell involves constant-time operations

# Space Complexity:
# - O(M*N) to store the dynamic programming table
# - We create a DP array with dimensions (M+1) × (N+1)

# INTUITION:
# The problem requires counting the total number of square submatrices with all 1's
# Key strategy:
# - Use dynamic programming to track square sizes at each cell
# - A square is formed when a cell can be the bottom-right corner of a square
# - The size of the square depends on the minimum square size of neighboring cells
# Example:
# Matrix:
# 1 0 1
# 1 1 1
# 1 1 1
# At (1,1), we can form a 1×1 square
# At (1,2) and (2,1), we can form a 2×2 square
# At (2,2), this becomes the bottom-right of a 3×3 square
# Each valid square contributes to the total count

# ALGO:
# 1. Create a DP table slightly larger than the input matrix
# 2. Iterate through each cell in the original matrix
# 3. For each cell with value 1:
#    - Calculate the maximum square size using minimum of three neighboring cells
#    - Add this size to the total count of squares
# 4. Return the total count of squares

class Solution:
   def countSquares(self, matrix: List[List[int]]) -> int:
       # Get matrix dimensions
       rowCount, colCount = len(matrix), len(matrix[0])
       
       # Create DP table to track square sizes
       # Add extra row and column for easier boundary handling
       squareSizes = [[0] * (colCount + 1) for _ in range(rowCount + 1)]
       
       # Total count of squares
       totalSquareCount = 0
       
       # Iterate through each cell in the matrix
       for rowIndex in range(rowCount):
           for colIndex in range(colCount):
               # Only process cells with value 1
               if matrix[rowIndex][colIndex]:
                   # Calculate maximum square size 
                   # By taking minimum of three neighboring cell square sizes
                   # And adding 1 to create a new square
                   squareSizes[rowIndex+1][colIndex+1] = (
                       1 + min(
                           squareSizes[rowIndex][colIndex+1],   # cell above
                           squareSizes[rowIndex+1][colIndex],   # cell to the left
                           squareSizes[rowIndex][colIndex]      # diagonal cell
                       )
                   )
                   
                   # Add current square size to total count
                   # Each value represents number of squares ending at this cell
                   totalSquareCount += squareSizes[rowIndex+1][colIndex+1]
       
       # Return total number of squares
       return totalSquareCount
