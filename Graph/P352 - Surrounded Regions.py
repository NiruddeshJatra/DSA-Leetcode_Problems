# Time Complexity:
# - O(M * N) where M is number of rows and N is number of columns
# - Each cell is visited at most once
# - Border traversal takes O(M + N)
# - Final matrix scan takes O(M * N)

# Space Complexity:
# - O(M * N) for visited set in worst case
# - O(M * N) for recursion stack in worst case
# - O(1) for directions array and other variables

# INTUITION:
# Only 'O's connected to border cannot be captured. We can:
# - Start DFS from border 'O's to mark all uncapturable cells
# - Any remaining 'O's are surrounded and can be captured
# Example:
# XXXX     XXXX
# XOOX  -> XXXX  
# XXOX     XXOX
# XOXX     XOXX
# Border O's and connected O's stay, others become X's

# ALGO:
# 1. Start DFS from each border 'O' to mark connected cells
# 2. Keep track of visited cells in a set
# 3. For each unvisited 'O' cell:
#    - If not connected to border (not visited)
#    - Change to 'X' as it can be captured
# 4. Original board is modified in place

class Solution:
   def solve(self, board: List[List[str]]) -> None:
       def markUncapturable(row: int, col: int) -> None:
           """Mark all 'O' cells connected to border using DFS"""
           visitedCells.add((row, col))
           
           # Check all 4 directions
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               
               if (0 <= newRow < numRows and 
                   0 <= newCol < numCols and 
                   (newRow, newCol) not in visitedCells and 
                   board[newRow][newCol] == "O"):
                   markUncapturable(newRow, newCol)
       
       if not board:
           return
           
       numRows, numCols = len(board), len(board[0])
       visitedCells = set()
       directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
       
       # Process border cells
       # Top and bottom borders
       for col in range(numCols):
           if (0, col) not in visitedCells and board[0][col] == "O":
               markUncapturable(0, col)
           if (numRows-1, col) not in visitedCells and board[numRows-1][col] == "O":
               markUncapturable(numRows-1, col)
       
       # Left and right borders
       for row in range(numRows):
           if (row, 0) not in visitedCells and board[row][0] == "O":
               markUncapturable(row, 0)
           if (row, numCols-1) not in visitedCells and board[row][numCols-1] == "O":
               markUncapturable(row, numCols-1)
       
       # Capture surrounded regions
       for row in range(numRows):
           for col in range(numCols):
               if (row, col) not in visitedCells and board[row][col] == "O":
                   board[row][col] = "X"
