"""
### Problem
The N-Queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other. Given an integer n, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

### Intuition
To solve the N-Queens problem, we can use backtracking. The idea is to place a queen on each row, ensuring that it does not conflict with already placed queens in terms of columns and diagonals.

### Approach
1. **Data Structures**: Use sets to keep track of columns (`col`), positive diagonals (`posDiagonal`), and negative diagonals (`negDiagonal`) that are already occupied by queens.
2. **Backtracking Function**: Define a recursive function `backtrack` to place queens row by row:
   - If the current row `r` equals `n`, it means all queens are placed correctly, and we add the current board configuration to the result list `ans`.
   - Iterate through each column `c` in the current row:
     - Check if placing a queen at `(r, c)` is safe by ensuring `c`, `r+c`, and `r-c` are not in `col`, `posDiagonal`, and `negDiagonal` respectively.
     - Place the queen, update the sets, and move to the next row by calling `backtrack(r + 1)`.
     - Remove the queen and revert the sets to explore other possibilities (backtrack).
3. **Initialization**: Initialize the board and start the backtracking process from the first row.
4. **Return**: Return the list of all valid board configurations.

### Time Complexity
The time complexity is O(N!), where N is the size of the board. This is because in the worst case, we are placing N queens on the board and each queen has N choices initially, N-1 choices for the next, and so on.

### Space Complexity
The space complexity is O(N) for the recursion stack and additional sets used to track the occupied columns and diagonals.

### Algorithm
1. Define the `backtrack` function:
   - If `r` equals `n`, convert the current board to the required format and add it to `ans`.
   - Iterate through each column `c` in the current row:
     - Check if the position `(r, c)` is safe.
     - Place the queen and update the sets.
     - Call `backtrack(r + 1)`.
     - Backtrack by removing the queen and reverting the sets.
2. Initialize and start the backtracking process.
3. Return the result list.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiagonal, negDiagonal = set(), set(), set()
        ans = []
        board = [["."]*n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                temp = ["".join(row) for row in board]
                ans.append(temp)
                return
            
            for c in range(n):
                if c not in col and (r+c) not in posDiagonal and (r-c) not in negDiagonal:
                    col.add(c)
                    posDiagonal.add(r+c)
                    negDiagonal.add(r-c)
                    board[r][c] = "Q"
                    backtrack(r+1)
                    col.remove(c)
                    posDiagonal.remove(r+c)
                    negDiagonal.remove(r-c)
                    board[r][c] = "."
                    
        backtrack(0)
        return ans
