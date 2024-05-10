# Time Complexity: O(m + n), where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem involves searching for a target element in a 2D matrix where each row and column is sorted in ascending order. 
# We can utilize a linear search approach to efficiently search for the target.
# 
# **Linear Search Approach**: We start at the top-right corner of the matrix. If the current element is equal to the target, 
# we return True. If the current element is greater than the target, we move left to explore smaller elements. If the current 
# element is smaller than the target, we move down to explore larger elements.
# 
# **Exploring Matrix**: By starting at the top-right corner, each move left decreases the column index, and each move down 
# increases the row index. This way, we efficiently explore the matrix until we find the target or exhaust the matrix.
# 
# **Handling Special Cases**: If the matrix is empty, we return False immediately. Additionally, if the target is smaller 
# than the top-right corner or larger than the bottom-left corner, we can immediately return False, as the target cannot 
# exist in the matrix.
# 
# **Termination Condition**: Keep iterating until we either find the target or exhaust the matrix. If the target is found, 
# return True; otherwise, return False.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Handling special cases
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
