# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix. 
# This is because we traverse every element in the matrix exactly once.
# Space Complexity: O(1), not counting the space required for the output list `ans`.

# INTUITION:
# The idea is to traverse the matrix in layers. We start with the outermost layer (top row, right column, bottom row, and left column) 
# and gradually move towards the inner layers by updating the boundaries after each traversal.

# ALGO:
# 1. Define the boundaries for the rows and columns: `row1`, `row2`, `col1`, and `col2`.
# 2. Traverse the matrix in the following order:
#    2.1. From left to right along the top boundary (`row1`), then move the top boundary down (`row1 += 1`).
#    2.2. From top to bottom along the right boundary (`col2`), then move the right boundary left (`col2 -= 1`).
#    2.3. From right to left along the bottom boundary (`row2`), then move the bottom boundary up (`row2 -= 1`).
#    2.4. From bottom to top along the left boundary (`col1`), then move the left boundary right (`col1 += 1`).
# 3. Repeat the above steps while the row and column boundaries have not crossed each other.
# 4. Return the `ans` list, which stores the elements in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Initialize row and column boundaries
        row1, row2 = 0, len(matrix) - 1
        col1, col2 = 0, len(matrix[0]) - 1
        ans = []  # List to store the spiral order traversal
        
        # Step 2: Traverse the matrix in spiral order
        while row1 <= row2 and col1 <= col2:
            # Step 2.1: Traverse from left to right on the top row
            for i in range(col1, col2 + 1):
                ans.append(matrix[row1][i])
            row1 += 1  # Move the top boundary down

            # Step 2.2: Traverse from top to bottom on the right column
            for i in range(row1, row2 + 1):
                ans.append(matrix[i][col2])
            col2 -= 1  # Move the right boundary left

            # Step 2.3: Traverse from right to left on the bottom row, if row1 <= row2
            if row1 <= row2:
                for i in range(col2, col1 - 1, -1):
                    ans.append(matrix[row2][i])
                row2 -= 1  # Move the bottom boundary up

            # Step 2.4: Traverse from bottom to top on the left column, if col1 <= col2
            if col1 <= col2:
                for i in range(row2, row1 - 1, -1):
                    ans.append(matrix[i][col1])
                col1 += 1  # Move the left boundary right
        
        # Step 3: Return the final spiral order
        return ans
