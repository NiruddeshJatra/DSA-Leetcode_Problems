# Time Complexity:
# - O(M * N), where M is the number of rows and N is the number of columns in the grid.
# - We potentially visit each cell in grid2 once during our DFS traversal.

# Space Complexity:
# - O(M * N) in the worst case for the recursion stack when the entire grid2 is filled with land (1s).

# INTUITION:
# A sub-island is an island in grid2 that is completely contained within an island in grid1.
# In other words, every cell that is land (1) in grid2 must also be land (1) in grid1 at the same position.
#
# We can approach this by exploring each island in grid2 using DFS, and checking if all its cells
# are also land in grid1. If we find any cell that is land in grid2 but water in grid1, then the
# island is not a sub-island.
#
# As we explore each island in grid2, we'll mark visited cells by changing them to 0 to avoid revisiting.

# ALGO:
# 1. Iterate through grid2 to find land cells (1).
# 2. When a land cell is found, use DFS to explore the entire island:
#    a. Check if the corresponding cell in grid1 is land (1). If not, mark this island as not a sub-island.
#    b. Mark the current cell as visited by changing its value to 0.
#    c. Recursively explore the four adjacent land cells.
# 3. After exploring each island, increment the count if it is a sub-island.
# 4. Return the total count of sub-islands.

class Solution:
   def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
       # Get grid dimensions
       numRows, numCols = len(grid2), len(grid2[0])
       
       # Possible movement directions: up, down, left, right
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       # Counter for valid sub-islands
       subIslandCount = 0
       
       def exploreIsland(row, col):
           # Flag to track if current island is a sub-island
           isValidSubIsland = True
           
           # If the corresponding cell in grid1 is water, this island cannot be a sub-island
           if grid1[row][col] == 0:
               isValidSubIsland = False
           
           # Mark current cell as visited
           grid2[row][col] = 0
           
           # Explore all four adjacent cells
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               
               # Check if the adjacent cell is valid and contains land in grid2
               if (0 <= newRow < numRows and 
                   0 <= newCol < numCols and 
                   grid2[newRow][newCol] == 1):
                   
                   # If any part of the island is not a sub-island, the whole island is not a sub-island
                   if not exploreIsland(newRow, newCol):
                       isValidSubIsland = False
           
           return isValidSubIsland
       
       # Traverse grid2 to find islands
       for row in range(numRows):
           for col in range(numCols):
               # If we find a land cell in grid2, explore the island
               if grid2[row][col] == 1:
                   # If the island is completely contained in an island in grid1, count it
                   if exploreIsland(row, col):
                       subIslandCount += 1
       
       return subIslandCount
