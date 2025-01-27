# Time Complexity:
# - O(M * N), where M is number of rows and N is number of columns
# - Need to traverse grid twice: once for counting ones and once for difference matrix

# Space Complexity:
# - O(M + N) for storing row and column counts
# - Not counting output matrix space as it's required

# INTUITION:
# Count ones in each row and column first, then compute difference matrix.
# Formula: 2 * (onesRow + onesCol) - (rowCount + colCount)
# This gives difference between ones and zeros since:
# zeros = totalLength - ones

# ALGO:
# 1. Count ones in each row and column by traversing grid once
# 2. For each cell (i,j) in result:
#    - Calculate 2*(onesInRow[i] + onesInCol[j]) - (rows + cols)
# 3. Return difference matrix

class Solution:
   def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
       rowCount = len(grid)
       colCount = len(grid[0])
       onesInRow = [0] * rowCount
       onesInCol = [0] * colCount
       diffMatrix = []

       # Count ones in each row and column
       for i in range(rowCount):
           for j in range(colCount):
               onesInRow[i] += grid[i][j]
               onesInCol[j] += grid[i][j]

       # Calculate difference matrix
       for i in range(rowCount):
           currentRow = []
           for j in range(colCount):
               diff = 2 * (onesInRow[i] + onesInCol[j]) - (rowCount + colCount)
               currentRow.append(diff)
           diffMatrix.append(currentRow)

       return diffMatrix
