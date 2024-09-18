# Time Complexity: O(n^2), where n is the number of rows (numRows). 
# Each row has a number of elements proportional to its index, so the total number of elements across all rows is 1 + 2 + 3 + ... + n = O(n^2).
# Space Complexity: O(n^2), as we are storing all the rows of the triangle in a 2D list.

# INTUITION:
# Pascal’s Triangle is a triangular array where the first and last elements of each row are 1, and each inner element is the sum of the two elements directly above it from the previous row. The challenge is to generate the first `numRows` of Pascal’s Triangle.

# ALGO:
# 1. Initialize the result list `res` with the first row containing just [1].
# 2. For each subsequent row (from 1 to numRows-1):
#    2.1 Create an empty list `row` for the current row.
#    2.2 For each element in the row (from 0 to the row index `i`), if the element is at the beginning or end of the row (i.e., index 0 or i), append 1 to `row`.
#    2.3 Otherwise, append the sum of the two elements directly above the current element from the previous row.
# 3. Append the completed row to the result list.
# 4. Return the result list containing all rows of Pascal’s Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Step 1: Initialize the result with the first row
        res = [[1]]
        
        # Step 2: Generate each row of Pascal's Triangle
        for i in range(1, numRows):
            row = []
            # Step 3: Generate each element in the row
            for j in range(i+1):
                # First and last elements of each row are always 1
                if j == 0 or j == i:
                    row.append(1)
                # Inner elements are the sum of the two elements above
                else:
                    row.append(res[i-1][j-1] + res[i-1][j])
            # Step 4: Append the row to the result
            res.append(row)
        
        # Step 5: Return the result list
        return res
