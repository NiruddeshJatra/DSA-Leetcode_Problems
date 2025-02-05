# Time Complexity:
# - O(M * N) where M is number of columns and N is number of rows
# - Each cell in grid is processed at most once
# - Queue operations take O(1) time
# - Initial scan of grid takes O(M * N)

# Space Complexity:
# - O(M * N) for queue in worst case when all oranges are rotten
# - Using input grid as visited array so no extra space
# - Directional array takes O(1) space

# INTUITION:
# BFS is perfect for this "spreading" type problem because:
# - Each minute, rot spreads one step in all directions
# - We need to process all oranges at current time before moving to next
# - Like a wavefront of rot expanding outward level by level
# Example:
# 2 1 1    2 2 1    2 2 2
# 1 1 0 -> 2 1 0 -> 2 2 0
# 0 1 1    0 1 1    0 2 2
# t=0      t=1      t=2  Returns 2 minutes

# ALGO:
# 1. Count fresh oranges and collect rotten orange positions
# 2. While queue not empty:
#    - Process all oranges at current level
#    - For each rotten orange:
#      * Check all 4 adjacent cells
#      * If fresh orange found, make it rotten
#      * Decrement fresh count
#    - Increment time after each level
# 3. Return time if all oranges rotten, -1 if impossible

class Solution:
   def orangesRotting(self, grid: List[List[int]]) -> int:
       numCols, numRows = len(grid[0]), len(grid)
       freshOranges = 0
       rottenQueue = deque()
       directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
       
       # Count fresh oranges and find initial rotten ones
       for row in range(numRows):
           for col in range(numCols):
               if grid[row][col] == 2:
                   rottenQueue.append((row, col))
               elif grid[row][col] == 1:
                   freshOranges += 1
       
       # Handle edge cases
       if freshOranges == 0:
           return 0
       if not rottenQueue:
           return -1
       
       timeElapsed = -1  # Start at -1 since we increment before checking first level
       
       # Process rotten oranges level by level
       while rottenQueue:
           timeElapsed += 1
           
           # Process all oranges at current level
           for _ in range(len(rottenQueue)):
               currentRow, currentCol = rottenQueue.popleft()
               
               # Check all 4 directions
               for dRow, dCol in directions:
                   newRow, newCol = currentRow + dRow, currentCol + dCol
                   
                   # If valid cell with fresh orange, make it rotten
                   if (0 <= newRow < numRows and 
                       0 <= newCol < numCols and 
                       grid[newRow][newCol] == 1):
                       
                       grid[newRow][newCol] = 2
                       freshOranges -= 1
                       rottenQueue.append((newRow, newCol))
       
       # Return result based on whether all oranges rotted
       return timeElapsed if freshOranges == 0 else -1
