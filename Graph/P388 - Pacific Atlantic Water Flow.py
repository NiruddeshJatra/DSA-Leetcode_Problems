# Time Complexity:
# - O(M * N), where M is the number of rows and N is the number of columns in the heights grid.
# - We perform DFS from each cell on the border, and each cell is visited at most twice (once for Pacific and once for Atlantic).

# Space Complexity:
# - O(M * N) for the sets storing cells that can reach each ocean and for the recursion stack in the worst case.

# INTUITION:
# Instead of checking for each cell if it can flow to both oceans (which would require running DFS from every cell),
# we approach the problem backwards. We start DFS from ocean borders and mark all cells that can flow to that ocean.
# Water can flow from a cell to its neighbor if the neighbor's height is greater than or equal to the current cell.
# By reversing our thinking, we run DFS from the ocean borders inward, and only visit cells that are higher or equal to their neighbors.
# 
# The cells that appear in both the Pacific and Atlantic sets are the ones from which water can flow to both oceans.

# ALGO:
# 1. Create two sets to track cells that can reach the Pacific and Atlantic oceans.
# 2. Run DFS from each border cell that touches the Pacific ocean, marking cells that can reach it.
# 3. Run DFS from each border cell that touches the Atlantic ocean, marking cells that can reach it.
# 4. Return the intersection of the two sets as our answer.
# Note: The DFS runs "uphill" - we only move to cells with height >= current cell.

class Solution:
   def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       # Edge case: empty grid
       if not heights or not heights[0]:
           return []
           
       # Get dimensions of the grid
       numRows, numCols = len(heights), len(heights[0])
       
       # Sets to store coordinates of cells that can reach each ocean
       pacificReachable = set()
       atlanticReachable = set()
       
       # Four possible directions: left, right, up, down
       directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
       
       def dfs(row, col, reachableSet):
           """
           DFS to mark all cells that can reach a particular ocean
           by going uphill from the ocean border.
           """
           # Add current cell to the reachable set
           reachableSet.add((row, col))
           
           # Check all four adjacent cells
           for dRow, dCol in directions:
               newRow, newCol = row + dRow, col + dCol
               
               # Skip if out of bounds or already visited
               if (newRow < 0 or newRow >= numRows or 
                   newCol < 0 or newCol >= numCols or 
                   (newRow, newCol) in reachableSet):
                   continue
               
               # Skip if water cannot flow from the adjacent cell to current cell
               # (Remember we're going backwards from ocean to land)
               if heights[newRow][newCol] < heights[row][col]:
                   continue
                   
               # Continue DFS from the adjacent cell
               dfs(newRow, newCol, reachableSet)
       
       # Run DFS from Pacific Ocean borders (top and left edges)
       for row in range(numRows):
           dfs(row, 0, pacificReachable)  # Left edge
           
       for col in range(numCols):
           dfs(0, col, pacificReachable)  # Top edge
           
       # Run DFS from Atlantic Ocean borders (bottom and right edges)
       for row in range(numRows):
           dfs(row, numCols - 1, atlanticReachable)  # Right edge
           
       for col in range(numCols):
           dfs(numRows - 1, col, atlanticReachable)  # Bottom edge
           
       # Find cells that can reach both oceans (intersection of the two sets)
       result = []
       for row in range(numRows):
           for col in range(numCols):
               if (row, col) in pacificReachable and (row, col) in atlanticReachable:
                   result.append([row, col])
                   
       return result
