# Time Complexity:
# - O(N^2) where N is dimension of grid
# - Each cell visited at most once
# - 8-directional check for each cell
# - Overall still O(N^2) as direction checks are constant

# Space Complexity:
# - O(N^2) for queue in worst case
# - Grid modified in place, no extra space
# - Overall space: O(N^2)

# INTUITION:
# Imagine a robot trying to cross a minefield where:
# - 0s are safe cells to move through
# - 1s are mines to avoid
# - Robot can move in 8 directions (like a king in chess)
# - Need shortest safe path from top-left to bottom-right
#
# BFS is perfect because:
# - Explores like ripples spreading from start
# - Each "ripple" represents cells reachable in K moves
# - First time we reach end is guaranteed shortest path
# - Like water finding shortest path through maze

# ALGORITHM:
# 1. Check if start/end cells are blocked
# 2. BFS from top-left:
#    - Track distance for each cell
#    - Try all 8 directions from current cell
#    - Mark visited cells to avoid cycles
#    - Queue contains (distance, row, col)
# 3. Return distance when reaching bottom-right
#    Or -1 if no path exists

class Solution:
   def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
       # Get grid dimensions
       gridSize = len(grid)
       
       # Check if start or end cell is blocked
       if grid[0][0] == 1 or grid[gridSize-1][gridSize-1] == 1:
           return -1
       
       # Initialize queue with starting position
       # Format: (distance, row, col)
       bfsQueue = [(1, 0, 0)]
       
       # Process cells level by level
       for currentDistance, currentRow, currentCol in bfsQueue:
           # Check if reached target
           if currentRow == gridSize - 1 and currentCol == gridSize - 1:
               return currentDistance
           
           # Try all 8 directions
           for deltaRow in [-1, 0, 1]:
               for deltaCol in [-1, 0, 1]:
                   # Calculate new position
                   newRow = currentRow + deltaRow
                   newCol = currentCol + deltaCol
                   
                   # Check if new position is valid:
                   # 1. Within grid bounds
                   # 2. Cell is not blocked (0)
                   if (0 <= newRow < gridSize and 
                       0 <= newCol < gridSize and 
                       grid[newRow][newCol] == 0):
                       
                       # Mark as visited to avoid cycles
                       grid[newRow][newCol] = 1
                       
                       # Add to queue with increased distance
                       bfsQueue.append((currentDistance + 1, newRow, newCol))
       
       # No path found
       return -1
