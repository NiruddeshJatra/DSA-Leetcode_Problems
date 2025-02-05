# Time Complexity:
# - O(M * N) where M is number of columns and N is number of rows
# - In worst case, we visit all cells in grid once
# - Each cell could be pushed to stack at most 4 times from neighbors

# Space Complexity:
# - O(M * N) for recursion stack in worst case
# - When whole image is filled with same color and shaped like a snake
# - Image modification is in-place so doesn't count towards space

# INTUITION:
# This is similar to how paint bucket tool works in image editors:
# - Start from initial pixel 
# - Spread to all connected pixels of same color
# - Change all these pixels to new color
# Example:
# Initial:  After fill(1,1,2):
# 1 1 1     2 2 2
# 1 1 0  -> 2 2 0
# 1 0 1     2 0 1

# ALGO:
# 1. Save original color at starting pixel
# 2. If new color is different from original:
#    - Use DFS to visit all connected pixels of original color
#    - Change each visited pixel to new color 
# 3. DFS explores in 4 directions (up, down, left, right)
# 4. Return modified image

class Solution:
   def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
       def fillColor(row: int, col: int) -> None:
           """Fill connected pixels of same color using DFS"""
           # Check bounds and if pixel matches original color
           if (0 <= row < numRows and 
               0 <= col < numCols and 
               image[row][col] == startColor):
               
               # Change pixel color
               image[row][col] = color
               
               # Fill in all 4 directions
               fillColor(row - 1, col)  # Up
               fillColor(row + 1, col)  # Down
               fillColor(row, col - 1)  # Left
               fillColor(row, col + 1)  # Right
       
       numCols = len(image[0])
       numRows = len(image)
       startColor = image[sr][sc]
       
       # Only fill if new color is different
       if startColor != color:
           fillColor(sr, sc)
           
       return image
