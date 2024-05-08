# Time Complexity: O(log(m) + log(n)), where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem involves searching for a target element in a 2D matrix where each row is sorted. We can utilize binary 
# search efficiently to search for the target.
# 
# **Binary Search on Rows**: We start by performing binary search on the rows of the matrix to find the potential row 
# where the target might exist.
# 
# **Finding the Row**: During the binary search on rows, if the target is smaller than the first element of the current 
# row, we move to the upper half of the matrix; if it's larger than the last element of the current row, we move to the 
# lower half; otherwise, we've found the row where the target might exist.
# 
# **Binary Search on Columns**: Once we've found the potential row, we perform binary search on that row to find the 
# target element.
# 
# **Handling Special Cases**: If the matrix is empty or the target is smaller than the first element of the first row 
# or larger than the last element of the last row, we can immediately return False, as the target cannot exist in the 
# matrix.
# 
# **Termination Condition**: Keep iterating until the search range is valid (i.e., until 'leftRow <= rightRow'). Once 
# the search range is exhausted, and the target is not found, return False.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Handling special cases
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        leftRow, rightRow = 0, len(matrix) - 1
        
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            
            if target < matrix[midRow][0]:
                rightRow = midRow - 1
            elif target > matrix[midRow][-1]:
                leftRow = midRow + 1
            else:
                l, r = 0, len(matrix[0]) - 1
                
                while l <= r:
                    mid = (l + r) // 2
                    if target < matrix[midRow][mid]:
                        r = mid - 1
                    elif target > matrix[midRow][mid]:
                        l = mid + 1
                    else:
                        return True
                return False
        
        return False
