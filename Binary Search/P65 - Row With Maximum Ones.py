# Time Complexity: O(m * n log n)
# Space Complexity: O(1)

# INTUITION:
# The problem requires finding the row with the maximum number of 1s in a binary matrix. 
# The approach leverages sorting each row and using binary search to efficiently count the number of 1s.
# By identifying the leftmost 1 in the sorted row, we can determine the count of 1s in that row.
# We keep track of the row with the highest count of 1s as we iterate through the matrix.

# ALGO:
# 1. Initialize a list `ans` to store the result, starting with [0, 0].
# 2. Initialize `cntOne` to keep track of the maximum number of 1s found.
# 3. Iterate through each row in the matrix:
#    a. Sort the current row.
#    b. Perform binary search to find the first occurrence of 1 in the sorted row:
#       - Initialize `l` and `r` for the binary search.
#       - Use a while loop to perform the binary search.
#       - Adjust `l` and `r` based on the value at `mid`.
#    c. Calculate the number of 1s in the row by subtracting the index of the first 1 from the row length.
#    d. If the current row has more 1s than `cntOne`, update `cntOne` and `ans` accordingly.
# 4. Return the `ans` list containing the row index and the count of 1s.

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        cntOne = 0
        for row in range(len(mat)):
            sortedRow = sorted(mat[row])
            l, r = 0, len(mat[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if sortedRow[mid] == 1:
                    r = mid - 1
                else:
                    l = mid + 1
            if cntOne < len(mat[0]) - l:
                cntOne = len(mat[0]) - l
                ans = [row, cntOne]

        return ans
