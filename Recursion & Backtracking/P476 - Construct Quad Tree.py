# Time Complexity:
# - O(N^2 * log N), where N is the side length of the grid (N x N).
# - We recursively divide the grid into 4 quadrants (log N levels), and for each region we check
#   if all values are the same which takes O(region_size^2) time in the worst case.
# - In the worst case, we might check O(N^2) cells at each level, leading to O(N^2 * log N).

# Space Complexity:
# - O(log N), for the recursion stack depth in a balanced quadtree.
# - In the worst case where no regions can be compressed, we might have O(N^2) nodes, but
#   the recursion depth is still O(log N) due to the divide-and-conquer approach.

# INTUITION:
# A QuadTree is a tree data structure where each internal node has exactly 4 children representing
# the 4 quadrants: topLeft, topRight, bottomLeft, bottomRight. Each leaf node represents a region
# where all values are the same (either all 0s or all 1s).
# 
# The key insight is to use divide-and-conquer: for any region, if all values are the same,
# create a leaf node. Otherwise, divide the region into 4 equal quadrants and recursively
# build subtrees for each quadrant.
# 
# Example: For a 4x4 grid, we first check if all 16 values are the same. If not, we divide
# into 4 2x2 regions and recursively process each. This continues until we reach regions
# where all values are uniform.

# ALGO:
# 1. Define helper function to check if all values in a region are the same
# 2. Define recursive function that builds quadtree for region starting at (row, col) with width:
#    a. If all values in region are the same:
#       - Create leaf node with the uniform value
#    b. Otherwise:
#       - Create internal node with isLeaf = False
#       - Recursively build 4 children for the 4 quadrants:
#         * topLeft: (row, col, width/2)
#         * topRight: (row, col + width/2, width/2)  
#         * bottomLeft: (row + width/2, col, width/2)
#         * bottomRight: (row + width/2, col + width/2, width/2)
# 3. Start recursion from (0, 0) with full grid width

"""
# Definition for a QuadTree node.
class Node:
   def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
       self.val = val
       self.isLeaf = isLeaf
       self.topLeft = topLeft
       self.topRight = topRight
       self.bottomLeft = bottomLeft
       self.bottomRight = bottomRight
"""

from typing import List

class Solution:
   def construct(self, grid: List[List[int]]) -> "Node":
       def buildQuadTree(startRow, startCol, regionWidth):
           def isUniformRegion(startRow, startCol, regionWidth):
               referenceValue = grid[startRow][startCol]
               for row in range(startRow, startRow + regionWidth):
                   for col in range(startCol, startCol + regionWidth):
                       if grid[row][col] != referenceValue:
                           return False
               return True

           # If all values in region are the same, create leaf node
           if isUniformRegion(startRow, startCol, regionWidth):
               return Node(grid[startRow][startCol] == 1, True)

           # Region has mixed values, create internal node with 4 children
           halfWidth = regionWidth // 2
           internalNode = Node(0, False)
           internalNode.topLeft = buildQuadTree(startRow, startCol, halfWidth)
           internalNode.topRight = buildQuadTree(startRow, startCol + halfWidth, halfWidth)
           internalNode.bottomLeft = buildQuadTree(startRow + halfWidth, startCol, halfWidth)
           internalNode.bottomRight = buildQuadTree(startRow + halfWidth, startCol + halfWidth, halfWidth)
           
           return internalNode

       return buildQuadTree(0, 0, len(grid))
