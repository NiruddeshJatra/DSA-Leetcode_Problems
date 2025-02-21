# Time Complexity:
# - O(N^2 × α(N^2)) where N is the grid dimension
# - Initial union-find grouping: O(N^2)
# - Find operations for each cell: O(N^2 × α(N^2))
# - Checking each 0 cell and its neighbors: O(N^2)

# Space Complexity:
# - O(N^2) for parent and size arrays
# - O(1) additional space for the set of roots when checking 0 cells

# INTUITION:
# We want to find the largest possible island after changing at most one 0 to 1.
# First, group existing land cells into islands using Union-Find.
# Then check each water cell (0) to see what size island we'd get by converting it,
# by adding up the sizes of unique adjacent islands.
#
# Example:
# [1,0,1]
# [0,0,0]
# [1,0,1]
#
# Initial islands: 4 single-cell islands
# Check center cell (0): Would connect all 4 islands -> size 4
# Check other 0s: Would connect 2 islands each -> size 3
# Answer: 4

# ALGO:
# 1. Initialize Union-Find with parent and size arrays
# 2. First pass: Group existing land cells (1s) into islands
#    - For each land cell, union with adjacent land cells
# 3. Find current maximum island size
# 4. Second pass: Try converting each water cell (0)
#    - For each water cell:
#      * Check all adjacent land cells
#      * Keep track of unique island roots
#      * Sum up sizes of all unique adjacent islands + 1
#      * Update maximum size if larger
# 5. Return maximum possible island size

class Solution:
   def largestIsland(self, grid: List[List[int]]) -> int:
       n = len(grid)
       # Initialize Union-Find data structures
       parent = list(range(n*n))  # Parent array
       size = [1] * (n*n)         # Size of each set
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
       def cellToIndex(x: int, y: int) -> int:
           return x * n + y
       
       def findParent(node: int) -> int:
           # Path compression
           if parent[node] != node:
               parent[node] = findParent(parent[node])
           return parent[node]
       
       def union(i: int, j: int) -> None:
           parentOfI = findParent(i)
           parentOfJ = findParent(j)
           
           if parentOfI == parentOfJ:
               return
               
           # Union by size
           if size[parentOfI] > size[parentOfJ]:
               parent[parentOfJ] = parentOfI
               size[parentOfI] += size[parentOfJ]
           else:
               parent[parentOfI] = parentOfJ
               size[parentOfJ] += size[parentOfI]
       
       # First pass: Group existing islands
       for x in range(n):
           for y in range(n):
               if grid[x][y] == 1:
                   for dx, dy in directions:
                       newX, newY = x + dx, y + dy
                       if (0 <= newX < n and 
                           0 <= newY < n and 
                           grid[newX][newY] == 1):
                           union(cellToIndex(x, y), cellToIndex(newX, newY))
       
       # Find current maximum island size
       maxIslandSize = 0
       for i in range(n):
           for j in range(n):
               root = findParent(cellToIndex(i, j))
               maxIslandSize = max(maxIslandSize, size[root])
       
       # Second pass: Try converting each 0 to 1
       for i in range(n):
           for j in range(n):
               if grid[i][j] == 0:
                   currentSize = 1  # Start with size 1 for current cell
                   seenRoots = set()  # Track unique island roots
                   
                   # Check all adjacent cells
                   for dx, dy in directions:
                       newX, newY = i + dx, j + dy
                       if (0 <= newX < n and 
                           0 <= newY < n and 
                           grid[newX][newY] == 1):
                           root = findParent(cellToIndex(newX, newY))
                           # Only add size if we haven't seen this island
                           if root not in seenRoots:
                               currentSize += size[root]
                               seenRoots.add(root)
                   
                   maxIslandSize = max(maxIslandSize, currentSize)
       
       return maxIslandSize
