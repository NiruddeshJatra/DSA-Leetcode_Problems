# Time Complexity:
# - O(M * N) where M is number of columns and N is number of rows
# - Each cell in grid is visited at most once
# - DFS visits each cell at most 4 times (once from each direction)

# Space Complexity:  
# - O(M * N) in worst case for recursion stack
# - When grid is filled with 1's and shaped like a snake
# - Grid modification is in-place so doesn't count towards space

# INTUITION:
# Think of the grid as connected components problem where:
# - Land cells ('1') are nodes
# - Adjacent land cells form edges
# - Each isolated group of connected land cells forms an island
# Example grid:
# 11000
# 11000  Has 2 islands:
# 00100  First island: Connected 1's in top left
# 00011  Second island: Connected 1's in bottom right

# ALGO:  
# 1. For each unvisited land cell ('1'):
#    - Mark it as visited ('#') 
#    - Use DFS to mark all connected land cells
#    - Increment island count
# 2. DFS explores in 4 directions (up, down, left, right)
#    and marks all reachable land cells
# 3. Return total number of islands found

class Solution:
   def numIslands(self, grid: List[List[str]]) -> int:
       def exploreIsland(row: int, col: int) -> None:
           """Mark all connected land cells as visited using DFS"""
           # Check bounds and if cell is unvisited land
           if (0 <= row < numRows and 
               0 <= col < numCols and 
               grid[row][col] == "1"):
               
               # Mark as visited
               grid[row][col] = "#"
               
               # Explore all 4 directions
               exploreIsland(row - 1, col)  # Up
               exploreIsland(row + 1, col)  # Down
               exploreIsland(row, col - 1)  # Left
               exploreIsland(row, col + 1)  # Right
       
       numCols = len(grid[0])
       numRows = len(grid)
       islandCount = 0
       
       # Find each island using DFS
       for i in range(numRows):
           for j in range(numCols):
               if grid[i][j] == '1':
                   exploreIsland(i, j)
                   islandCount += 1
                   
       return islandCount
