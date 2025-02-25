# Time Complexity:
# - O(M * N), where M is the number of rows and N is the number of columns in the grid.
# - We visit each cell at most once during our DFS traversal.

# Space Complexity:
# - O(M * N) in the worst case for the recursion stack when the entire grid is filled with land (1s).

# INTUITION:
# The perimeter of an island is the total number of edges that separate land cells from water or the boundary of the grid.
# Each land cell can contribute between 0 and 4 to the perimeter, depending on how many of its adjacent cells are water
# or outside the grid.
# 
# The key insight is that a land cell contributes to the perimeter for each adjacent cell that is either:
# 1. Outside the grid (beyond the edges)
# 2. A water cell (has value 0)
#
# We can use DFS to explore the island (there is only one island per the problem description) and count the
# perimeter edges as we go.

# ALGO:
# 1. Iterate through the grid to find the first land cell (value 1).
# 2. Once found, use DFS to explore the entire island:
#    a. If we encounter water (0) or go outside the grid, add 1 to the perimeter.
#    b. If we encounter an already visited cell (-1), add 0 to the perimeter.
#    c. Mark the current cell as visited by changing its value to -1.
#    d. Recursively explore all four adjacent cells and accumulate the perimeter contributions.
# 3. Return the total perimeter calculated during DFS.

class Solution:
   def islandPerimeter(self, grid: List[List[int]]) -> int:
       # Get grid dimensions
       numRows, numCols = len(grid), len(grid[0])
       
       # Possible movement directions: up, down, left, right
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       def calculatePerimeter(row, col):
           # If out of bounds or water cell, contributes 1 to perimeter
           if (row < 0 or row >= numRows or 
               col < 0 or col >= numCols or 
               grid[row][col] == 0):
               return 1
           
           # If already visited, contributes 0 to perimeter
           if grid[row][col] == -1:
               return 0
           
           # Mark current cell as visited
           grid[row][col] = -1
           
           # Initialize perimeter contribution for current cell
           perimeterCount = 0
           
           # Check all four adjacent cells
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               perimeterCount += calculatePerimeter(newRow, newCol)
           
           return perimeterCount
       
       # Find the first land cell and start DFS from there
       for row in range(numRows):
           for col in range(numCols):
               if grid[row][col] == 1:
                   # There is exactly one island, so we can return as soon as we find it
                   return calculatePerimeter(row, col)
       
       # If no land cells found
       return 0
