# Time Complexity:
# - O(M * N * log(M * N)) where M and N are dimensions of grid
# - Each cell can be visited multiple times, and each heap operation takes log(M*N)
# - In worst case, we might need to push/pop each cell multiple times as we find better paths

# Space Complexity:
# - O(M * N) for the distance array to store minimum efforts
# - O(M * N) for the heap in worst case where we need to store all cells

# INTUITION:
# We need to find path from top-left to bottom-right minimizing maximum absolute difference between adjacent cells.
# This is similar to finding shortest path, but instead of sum of weights, we care about maximum edge weight.
# Think of it like finding the "smoothest" path where we want to minimize the steepest climb/descent.
# Example: In grid [[1,2,2],[3,8,2],[5,3,5]], path 1->2->2->2->5 gives effort 3 (max diff is |8-2|=6)
# instead of going through middle cell.

# ALGO:
# 1. Initialize distance matrix with infinity except starting point
# 2. Use min heap to store (effort, row, col) tuples
# 3. For each cell popped from heap:
#    - Check all 4 adjacent cells
#    - Calculate maximum effort needed (max of current effort and new height difference)
#    - If new effort is less than known effort for that cell:
#      * Update distance
#      * Add cell to heap with new effort
# 4. Return final effort for bottom-right cell

from typing import List
import heapq

class Solution:
   def minimumEffortPath(self, heights: List[List[int]]) -> int:
       numRows, numCols = len(heights), len(heights[0])
       
       # Initialize distance matrix with infinity
       minEfforts = [[float('inf')] * numCols for _ in range(numRows)]
       minEfforts[0][0] = 0
       
       # Initialize min heap with (effort, row, col)
       effortHeap = [(0, 0, 0)]
       
       # Possible movements: up, down, left, right
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       while effortHeap:
           currentEffort, currentRow, currentCol = heapq.heappop(effortHeap)
           
           # Check all adjacent cells
           for deltaRow, deltaCol in directions:
               newRow, newCol = currentRow + deltaRow, currentCol + deltaCol
               
               # Check if new position is within grid
               if 0 <= newRow < numRows and 0 <= newCol < numCols:
                   # Calculate maximum effort needed for this move
                   newEffort = max(
                       currentEffort,
                       abs(heights[newRow][newCol] - heights[currentRow][currentCol])
                   )
                   
                   # If we found a path with less effort, update and explore
                   if newEffort < minEfforts[newRow][newCol]:
                       minEfforts[newRow][newCol] = newEffort
                       heapq.heappush(effortHeap, (newEffort, newRow, newCol))
       
       # Return minimum effort to reach bottom-right cell
       return minEfforts[numRows-1][numCols-1]
