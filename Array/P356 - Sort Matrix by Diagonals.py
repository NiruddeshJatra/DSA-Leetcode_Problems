# Time Complexity:
# - O(K * log K) for each diagonal where K is length of diagonal
# - Total is O(N^2 * log N) since longest diagonal has length N
# - Each element is sorted exactly once
# - We process 2N-1 diagonals in total

# Space Complexity:
# - O(N) additional space for temporary array
# - Longest diagonal has N elements
# - Matrix is modified in-place
# - All other variables take O(1) space

# INTUITION:
# The key observation is that adjacent elements along diagonals
# should be sorted, which gives us this strategy:
# 1. Process each diagonal from bottom-left to top-right
# 2. First N diagonals start from last row and go up-left
# 3. Remaining N-1 diagonals start from rightmost column and go up-left
# 4. For each diagonal:
#    - Collect elements in temp array
#    - Sort them (reverse for first N diagonals)
#    - Put back in same positions
# 
# Example for 3x3 matrix:
# Processing order:
# 5 3 1     Each number represents
# 4 2 0     the diagonal group
# 3 1 0     it belongs to

class Solution:
   def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
       matrixSize = len(grid)
       totalDiagonals = 2 * matrixSize - 1
       
       # Process each diagonal
       for diagonalNum in range(totalDiagonals):
           if diagonalNum < matrixSize:
               # First N diagonals starting from bottom row
               currentRow = matrixSize - 1
               currentCol = diagonalNum
               diagonalElements = []
               
               # Collect elements along diagonal
               for i in range(diagonalNum + 1):
                   diagonalElements.append(grid[currentRow][currentCol])
                   currentRow -= 1
                   currentCol -= 1
               
               # Sort in descending order for first N diagonals
               diagonalElements.sort(reverse=True)
               
               # Put sorted elements back
               currentRow = matrixSize - 1
               currentCol = diagonalNum
               for i in range(diagonalNum + 1):
                   grid[currentRow][currentCol] = diagonalElements.pop()
                   currentRow -= 1
                   currentCol -= 1
                   
           else:
               # Remaining N-1 diagonals starting from rightmost column
               currentRow = 2 * (matrixSize - 1) - diagonalNum
               currentCol = matrixSize - 1
               diagonalElements = []
               
               # Collect elements along diagonal
               for i in range(totalDiagonals - diagonalNum):
                   diagonalElements.append(grid[currentRow][currentCol])
                   currentRow -= 1
                   currentCol -= 1
               
               # Sort in ascending order for remaining diagonals 
               diagonalElements.sort()
               
               # Put sorted elements back
               currentRow = 2 * (matrixSize - 1) - diagonalNum
               currentCol = matrixSize - 1
               for i in range(totalDiagonals - diagonalNum):
                   grid[currentRow][currentCol] = diagonalElements.pop()
                   currentRow -= 1
                   currentCol -= 1
                   
       return grid
