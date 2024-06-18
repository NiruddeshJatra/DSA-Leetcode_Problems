"""
### Problem
Given a partially filled 9x9 Sudoku board, fill in the board such that each row, each column, and each of the nine 3x3 sub-boxes contain the digits 1 to 9 exactly once. The empty cells in the board are denoted by '.'.

### Intuition
To solve the Sudoku puzzle, we can use a backtracking approach. Starting from the top-left cell, we attempt to place each digit from 1 to 9 in each empty cell, ensuring that the placement is valid according to the Sudoku rules. If a placement leads to a solution, we return true. If no digit can be placed in a cell without violating the rules, we backtrack and try a different digit in the previous cell.

### Approach
1. **Validity Check**: Define a helper function `isValid` to check if placing a digit in a given cell is valid according to the Sudoku rules:
    - The digit must not already exist in the current row.
    - The digit must not already exist in the current column.
    - The digit must not already exist in the current 3x3 sub-box.
2. **Backtracking Function**: Define a recursive function `solve` to fill the board:
    - If the current cell is the last cell in the row, move to the next row.
    - If the current cell is empty, try placing each digit from 1 to 9 and recursively solve the board.
    - If a placement is valid, place the digit and move to the next cell.
    - If the placement leads to a solution, return true.
    - If no placement is valid, reset the cell and backtrack.
3. **Initialization**: Start the backtracking process from the top-left cell `(0, 0)`.

### Time Complexity
The time complexity is O(9^(n^2)), where n is the size of the board (9). In the worst case, we might need to try each of the 9 possible digits for each of the 81 cells.

### Space Complexity
The space complexity is O(n^2) for the recursion stack, where n is the size of the board (9).

### Algorithm
1. Define the `isValid` function to check if placing a digit in a cell is valid.
2. Define the `solve` function to recursively fill the board:
    - If the current cell is the last cell in the row, move to the next row.
    - If the current cell is empty, try placing each digit from 1 to 9 and recursively solve the board.
    - If a placement is valid, place the digit and move to the next cell.
    - If the placement leads to a solution, return true.
    - If no placement is valid, reset the cell and backtrack.
3. Initialize and start the backtracking process from the top-left cell `(0, 0)`.
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row, col, c):
            for i in range(9):
                if board[row][i] == c:
                    return False
                if board[i][col] == c:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False

            return True

        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for c in "123456789":
                    if isValid(row, col, c):
                        board[row][col] = c
                        if solve(row, col + 1):
                            return True
                        board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)

        solve(0, 0)
