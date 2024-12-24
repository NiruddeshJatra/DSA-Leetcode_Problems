# Time Complexity: O(n^2)
# - The matrix has n x n elements, and each element is visited exactly once during the traversal.
# - Hence, the time complexity is O(n^2).

# Space Complexity: O(n^2)
# - The algorithm creates a matrix of size n x n, which requires O(n^2) space.
# - No additional space is used apart from a few variables.

# INTUITION:
# The problem requires generating a matrix of size `n x n` where the elements are filled in a spiral order starting from 1.
# To achieve this, we use a systematic approach to traverse the matrix layer by layer:
# - First fill the top row from left to right.
# - Then fill the right column from top to bottom.
# - Followed by the bottom row from right to left.
# - Finally, fill the left column from bottom to top.
# This process continues until all elements in the matrix are filled.

# ALGO:
# 1. Initialize an `n x n` matrix filled with zeros.
# 2. Define pointers for the boundaries of the current layer:
#    - `startRow` and `endRow` for the top and bottom boundaries.
#    - `startCol` and `endCol` for the left and right boundaries.
# 3. Start filling the matrix in a spiral pattern:
#    - Fill the top row from left to right, then increment `startRow`.
#    - Fill the right column from top to bottom, then decrement `endCol`.
#    - Fill the bottom row from right to left, then decrement `endRow`.
#    - Fill the left column from bottom to top, then increment `startCol`.
# 4. Repeat until all elements are filled.
# 5. Return the filled matrix.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Initialize pointers and variables
        startRow, startCol, endRow, endCol = 0, 0, n - 1, n - 1
        num = 1  # Start filling the matrix from 1

        # Fill the matrix in a spiral pattern
        while startRow <= endRow and startCol <= endCol:
            # Fill the top row
            for j in range(startCol, endCol + 1):
                matrix[startRow][j] = num
                num += 1
            startRow += 1

            # Fill the right column
            for i in range(startRow, endRow + 1):
                matrix[i][endCol] = num
                num += 1
            endCol -= 1

            # Fill the bottom row (if applicable)
            if startRow <= endRow:
                for j in range(endCol, startCol - 1, -1):
                    matrix[endRow][j] = num
                    num += 1
                endRow -= 1

            # Fill the left column (if applicable)
            if startCol <= endCol:
                for i in range(endRow, startRow - 1, -1):
                    matrix[i][startCol] = num
                    num += 1
                startCol += 1

        # Return the resulting spiral matrix
        return matrix
