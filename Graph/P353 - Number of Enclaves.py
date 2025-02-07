# Time Complexity:
# - O(M * N) where M is number of rows and N is number of columns
# - Each cell is visited at most once in DFS
# - Border traversal takes O(M + N)
# - Final count traversal takes O(M * N)

# Space Complexity:
# - O(M * N) for visited set in worst case
# - O(M * N) for recursion stack in worst case when all cells form one path
# - O(1) for directions array and counter variable

# INTUITION:
# Similar to Surrounded Regions, but now we want to:
# - Find land cells (1's) that can't reach border
# - Count these "trapped" land cells
# Example:
# 0 0 0 0    Visited marks border-connected 1's:  Count unmarked 1's:
# 1 1 0 0    0 0 0 0                             0 0 0 0
# 0 1 1 0 -> 1 1 0 0                          -> 0 0 1 0
# 0 0 0 0    0 0 1 0                             0 0 0 0
# Result: 1 (only the middle 1 is trapped)

# ALGO:
# 1. Start DFS from each border land cell (1)
# 2. Mark all land cells connected to border as visited
# 3. Count remaining unvisited land cells
#    - These are the enclaves (can't reach border)
# 4. Return total count of enclaves

class Solution:
   def numEnclaves(self, board: List[List[int]]) -> int:
       def markBorderConnected(row: int, col: int) -> None:
           """Mark all land cells connected to border using DFS"""
           visitedCells.add((row, col))
           
           # Check all 4 directions
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               
               if (0 <= newRow < numRows and 
                   0 <= newCol < numCols and 
                   (newRow, newCol) not in visitedCells and 
                   board[newRow][newCol] == 1):
                   markBorderConnected(newRow, newCol)
       
       numRows, numCols = len(board), len(board[0])
       visitedCells = set()
       directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
       
       # Process border cells
       # Top and bottom borders
       for col in range(numCols):
           if (0, col) not in visitedCells and board[0][col] == 1:
               markBorderConnected(0, col)
           if (numRows-1, col) not in visitedCells and board[numRows-1][col] == 1:
               markBorderConnected(numRows-1, col)
       
       # Left and right borders
       for row in range(numRows):
           if (row, 0) not in visitedCells and board[row][0] == 1:
               markBorderConnected(row, 0)
           if (row, numCols-1) not in visitedCells and board[row][numCols-1] == 1:
               markBorderConnected(row, numCols-1)
       
       # Count unvisited land cells (enclaves)
       enclaveCount = 0
       for row in range(numRows):
           for col in range(numCols):
               if (row, col) not in visitedCells and board[row][col] == 1:
                   enclaveCount += 1
                   
       return enclaveCount
