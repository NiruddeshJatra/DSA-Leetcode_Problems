# Time Complexity: O(m log n)
# Space Complexity: O(1)

# INTUITION:
# The problem requires finding a peak element in a 2D grid, where a peak is defined as an element that is greater than or equal to its neighbors. 
# We can use a binary search approach on the columns of the matrix to efficiently locate a peak.
# By selecting the middle column and finding the maximum element in that column, we can determine which direction to continue the search.
# This process ensures that we converge to a peak element in logarithmic time with respect to the number of columns.

# ALGO:
# 1. Define a helper function `maxElement` that takes a column index and returns the row index of the maximum element in that column.
# 2. Initialize `l` and `r` to represent the leftmost and rightmost column indices.
# 3. Use a while loop to perform binary search on the columns:
#    a. Calculate `mid` as the middle column index.
#    b. Use `maxElement` to find the row index of the maximum element in the `mid` column.
#    c. Check if the element at `mat[row][mid]` is a peak:
#       - It should be greater than or equal to its left neighbor (if it exists).
#       - It should be greater than or equal to its right neighbor (if it exists).
#    d. If `mat[row][mid]` is a peak, return its indices `[row, mid]`.
#    e. If the peak is not found, adjust the search range based on the neighbors' values:
#       - Move to the right half if the middle element is greater than its left neighbor.
#       - Move to the left half otherwise.

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def maxElement(col):
            maxVal, row = -1, 0
            for i in range(len(mat)):
                if mat[i][col] > maxVal:
                    maxVal = mat[i][col]
                    row = i
            return row

        l, r = 0, len(mat[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            row = maxElement(mid)
            if (mid == 0 or mat[row][mid] > mat[row][mid - 1]) and (mid == len(mat[0]) - 1 or mat[row][mid] > mat[row][mid + 1]):
                return [row, mid]
            elif mid == 0 or mat[row][mid] > mat[row][mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
