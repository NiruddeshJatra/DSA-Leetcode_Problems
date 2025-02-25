# Time Complexity:
# - O(M * N), where M is the number of rows and N is the number of columns in the grid.
# - We potentially visit each cell in the grid once during our traversal.

# Space Complexity:
# - O(M * N) in the worst case for the recursion stack when the entire grid is filled with land (1s).

# INTUITION:
# The problem asks us to find the largest island (connected 1s) in a 2D grid. We can solve this by traversing
# the grid and using DFS to explore each island when we encounter a land cell (1). For each island, we'll count
# its area (number of connected land cells) and keep track of the maximum area found.
#
# To avoid revisiting cells and prevent infinite loops, we'll mark each visited cell by changing its value
# from 1 to 0 (essentially "sinking" the island as we explore it).
#
# The key insight is that we can calculate the area of an island recursively:
# - Each land cell contributes 1 to the area
# - The total area is the sum of the current cell (1) plus the areas of all adjacent land cells

# ALGO:
# 1. Iterate through each cell in the grid.
# 2. When a land cell (1) is found, use DFS to explore the entire island:
#    a. Mark the current cell as visited by changing its value to 0.
#    b. Add 1 to the area (for the current cell).
#    c. Recursively explore the four adjacent cells (up, down, left, right).
#    d. Sum up the areas from all recursive calls.
# 3. Keep track of the maximum area found during the traversal.
# 4. Return the maximum area.

class Solution:
   def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       # Get grid dimensions
       numRows, numCols = len(grid), len(grid[0])
       
       # Possible movement directions: up, down, left, right
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       # Variable to track maximum island area
       maxIslandArea = 0
       
       def exploreIsland(row, col):
           # Mark current cell as visited by changing it to 0
           grid[row][col] = 0
           
           # Start with area of 1 for current cell
           currentArea = 1
           
           # Explore all four adjacent cells
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               
               # Check if the adjacent cell is valid and contains land
               if (0 <= newRow < numRows and 
                   0 <= newCol < numCols and 
                   grid[newRow][newCol] == 1):
                   # Add the area of connected land from this direction
                   currentArea += exploreIsland(newRow, newCol)
           
           return currentArea
       
       # Traverse the entire grid
       for row in range(numRows):
           for col in range(numCols):
               # If we find a land cell, explore the island it belongs to
               if grid[row][col] == 1:
                   # Update maximum area if current island is larger
                   islandArea = exploreIsland(row, col)
                   maxIslandArea = max(maxIslandArea, islandArea)
       
       return maxIslandArea
