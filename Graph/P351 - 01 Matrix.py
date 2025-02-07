# Time Complexity:
# - O(M * N) where M is number of rows and N is number of columns
# - Each cell is pushed to queue at most once
# - Initial matrix scan takes O(M * N)
# - BFS process takes O(M * N) as each cell processed once

# Space Complexity:
# - O(M * N) for distance matrix
# - O(M * N) for queue in worst case when all cells are 0s
# - O(1) for directions array and other variables

# INTUITION:
# We can solve this using a multi-source BFS where:
# - All 0 cells are starting points with distance 0
# - BFS propagates minimum distances level by level
# - Each level represents cells one step further from nearest 0
# Example:
# Input:  Distance matrix after BFS:
# 0 0 0   0 0 0
# 0 1 0   0 1 0
# 1 1 1   1 2 1

# ALGO:
# 1. Create distance matrix initialized to infinity
# 2. Find all 0s, set their distance to 0 and add to queue
# 3. While queue not empty:
#    - Get current cell
#    - Check all 4 adjacent cells
#    - If new distance is smaller, update and add to queue
# 4. Return completed distance matrix

class Solution:
   def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       numRows, numCols = len(mat), len(mat[0])
       distanceMatrix = [[float('inf')] * numCols for _ in range(numRows)]
       cellQueue = deque()
       directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
       
       # Initialize distances for 0 cells
       for row in range(numRows):
           for col in range(numCols):
               if mat[row][col] == 0:
                   distanceMatrix[row][col] = 0
                   cellQueue.append((row, col))
       
       # Process cells level by level
       while cellQueue:
           currentRow, currentCol = cellQueue.popleft()
           currentDist = distanceMatrix[currentRow][currentCol]
           
           # Check all 4 directions
           for dRow, dCol in directions:
               newRow, newCol = currentRow + dRow, currentCol + dCol
               
               # If valid cell and new distance is smaller
               if (0 <= newRow < numRows and 
                   0 <= newCol < numCols and 
                   distanceMatrix[newRow][newCol] > currentDist + 1):
                   
                   distanceMatrix[newRow][newCol] = currentDist + 1
                   cellQueue.append((newRow, newCol))
       
       return distanceMatrix
