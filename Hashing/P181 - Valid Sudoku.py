# Time Complexity: O(1)  
# - The Sudoku board is always 9x9, so the number of iterations is constant.  
# - Checking and updating dictionaries for rows, columns, and boxes are O(1) operations.

# Space Complexity: O(1)  
# - The dictionaries for rows, columns, and boxes store at most 81 values (one for each cell on the board).  
# - The space usage is constant as the board size is fixed.

# INTUITION:  
# The problem requires checking whether a given Sudoku board is valid according to Sudoku rules.  
# To do this, we must ensure:  
# 1. Each row contains unique numbers.  
# 2. Each column contains unique numbers.  
# 3. Each 3x3 sub-box contains unique numbers.  
# By dividing the board into rows, columns, and boxes, and tracking the values encountered in each,  
# we can efficiently validate the Sudoku board. Using dictionaries to store occurrences of numbers helps us quickly identify duplicates.

# ALGORITHM:  
# 1. Create dictionaries to track numbers seen in each row, column, and box.  
# 2. Iterate through the board:  
#    - Skip empty cells (".").  
#    - Calculate the box index for the current cell using the formula `(row // 3) * 3 + col // 3`.  
#    - Check if the value is already present in the corresponding row, column, or box.  
#    - If found, return `False`.  
#    - Otherwise, add the value to the corresponding row, column, and box dictionaries.  
# 3. If no conflicts are found, return `True`.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to track values in rows, columns, and boxes
        rowValues = [{} for _ in range(9)]
        columnValues = [{} for _ in range(9)]
        boxValues = [{} for _ in range(9)]

        # Iterate through each cell in the board
        for row in range(9):
            for col in range(9):
                # Calculate the index of the corresponding 3x3 box
                boxIndex = (row // 3) * 3 + col // 3
                value = board[row][col]

                # Skip empty cells
                if value == ".":
                    continue

                # Check for duplicates in the row, column, or box
                if value in rowValues[row] or value in columnValues[col] or value in boxValues[boxIndex]:
                    return False

                # Add the value to the row, column, and box dictionaries
                rowValues[row][value] = 1
                columnValues[col][value] = 1
                boxValues[boxIndex][value] = 1

        # If no conflicts, the board is valid
        return True
