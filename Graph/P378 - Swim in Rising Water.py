# Time Complexity:
# - O(N^2 log N) where N is the grid dimension
# - Each cell is pushed/popped from heap once
# - Each heap operation takes O(log N^2) = O(log N)

# Space Complexity:
# - O(N^2) for the heap and seen set in worst case
# - Both heap and seen set could contain all grid cells

# INTUITION:
# We want to find minimum time to reach bottom right with water level constraints.
# Use Dijkstra's algorithm, where "distance" is max water level needed so far.
# Always expand to next cell with lowest elevation to minimize max water level.
#
# Example:
# [0,2]
# [1,3]
#
# Start at (0,0)=0
# Options: (0,1)=2, (1,0)=1
# Take (1,0)=1: max level = 1
# Options: (1,1)=3
# Take (0,1)=2: max level = 2
# Take (1,1)=3: max level = 3
# Answer = 3

# ALGO:
# 1. Initialize min heap with starting cell
# 2. While heap not empty:
#    - Pop cell with minimum elevation
#    - Update max water level needed
#    - If reached target, return result
#    - Add all unvisited neighbors to heap
# 3. Keep track of visited cells to avoid cycles

class Solution:
   def swimInWater(self, grid: List[List[int]]) -> int:
       # Initialize min heap with starting point
       minHeap = [(grid[0][0], 0, 0)]  # (elevation, row, col)
       
       # Directions for 4-way movement
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       # Track visited cells
       visited = {(0, 0)}
       
       # Track maximum water level needed
       maxWaterLevel = 0
       
       n = len(grid)
       
       while True:
           # Get next cell with minimum elevation
           elevation, row, col = heapq.heappop(minHeap)
           
           # Update maximum water level needed
           maxWaterLevel = max(maxWaterLevel, elevation)
           
           # If reached target, return result
           if row == col == n - 1:
               return maxWaterLevel
           
           # Check all neighbors
           for dx, dy in directions:
               newRow, newCol = row + dx, col + dy
               
               # If valid unvisited neighbor
               if (0 <= newRow < n and 
                   0 <= newCol < n and 
                   (newRow, newCol) not in visited):
                   
                   visited.add((newRow, newCol))
                   heapq.heappush(minHeap, 
                                (grid[newRow][newCol], newRow, newCol))
