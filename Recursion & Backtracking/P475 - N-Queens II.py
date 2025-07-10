# Time Complexity:
# - O(N!), where N is the size of the chessboard.
# - In the worst case, we explore all possible placements. For the first row we have N choices,
#   for the second row we have at most N-1 valid choices, and so on, leading to N! combinations.
# - The actual complexity is better due to pruning, but N! represents the upper bound.

# Space Complexity:
# - O(N), for the recursion stack depth (N levels) and the three sets storing visited positions.
# - Each set can contain at most N elements at any time.

# INTUITION:
# The N-Queens problem asks for the number of ways to place N queens on an N×N chessboard
# such that no two queens attack each other. Queens can attack horizontally, vertically, and diagonally.
# 
# We use backtracking to try placing queens row by row. For each row, we try every column position
# and check if it's safe (no conflicts with previously placed queens). We track three types of conflicts:
# 1. Column conflicts: queens in the same column attack each other
# 2. Main diagonal conflicts: queens on diagonals where row-col is constant
# 3. Anti-diagonal conflicts: queens on diagonals where row+col is constant
# 
# Example: For a 4×4 board, one valid solution places queens at (0,1), (1,3), (2,0), (3,2).
# We use sets to efficiently track which columns and diagonals are already occupied.

# ALGO:
# 1. Initialize counters and sets to track occupied columns and diagonals
# 2. Define backtrack function that tries to place queens starting from given row:
#    a. Base case: if we've placed queens in all N rows, increment count
#    b. For each column in current row:
#       - Calculate diagonal identifiers: mainDiag = row-col, antiDiag = row+col
#       - Check if column and both diagonals are free
#       - If safe: place queen (add to sets), recurse to next row, then backtrack (remove from sets)
# 3. Start backtracking from row 0
# 4. Return total count of valid solutions

class Solution:
   def totalNQueens(self, n: int) -> int:
       solutionCount = 0
       occupiedColumns = set()
       occupiedMainDiagonals = set()    # row - col is constant
       occupiedAntiDiagonals = set()    # row + col is constant

       def backtrackQueens(currentRow):
           nonlocal solutionCount
           
           # Base case: successfully placed all N queens
           if currentRow == n:
               solutionCount += 1
               return

           # Try placing queen in each column of current row
           for currentCol in range(n):
               mainDiagonalId = currentRow - currentCol
               antiDiagonalId = currentRow + currentCol
               
               # Check if position is safe (no conflicts)
               if (currentCol not in occupiedColumns and 
                   mainDiagonalId not in occupiedMainDiagonals and 
                   antiDiagonalId not in occupiedAntiDiagonals):
                   
                   # Place queen: mark column and diagonals as occupied
                   occupiedColumns.add(currentCol)
                   occupiedMainDiagonals.add(mainDiagonalId)
                   occupiedAntiDiagonals.add(antiDiagonalId)
                   
                   # Recurse to next row
                   backtrackQueens(currentRow + 1)
                   
                   # Backtrack: remove queen and free up column and diagonals
                   occupiedColumns.remove(currentCol)
                   occupiedMainDiagonals.remove(mainDiagonalId)
                   occupiedAntiDiagonals.remove(antiDiagonalId)

       backtrackQueens(0)
       return solutionCount
