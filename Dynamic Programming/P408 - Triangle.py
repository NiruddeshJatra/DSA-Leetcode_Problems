# Time Complexity:
# - O(n²), where n is the number of rows in the triangle.
# - We process each element in the triangle exactly once.
# - In a triangle with n rows, there are n*(n+1)/2 elements in total.

# Space Complexity:
# - O(n), where n is the number of rows in the triangle.
# - We use a single array of size n+1 to store the dynamic programming states.

# INTUITION:
# This problem asks for the minimum path sum from the top to the bottom of a triangle.
# While we could solve it top-down, the bottom-up approach is more elegant and efficient.
#
# The key insight is that to find the minimum path to any element, we need to know the minimum
# paths to the two elements below it. By starting from the bottom row and working our way up,
# we can compute these minimums efficiently.
#
# For example, with triangle [[2],[3,4],[6,5,7],[4,1,8,3]]:
# - Starting from the bottom row [4,1,8,3], these are the initial minimum path sums
# - For the row above [6,5,7], the minimum path sums become [6+min(4,1), 5+min(1,8), 7+min(8,3)] = [7,6,10]
# - For the next row [3,4], we get [3+min(7,6), 4+min(6,10)] = [9,10]
# - For the top row [2], we get [2+min(9,10)] = [11]
# The answer is 11.

# ALGO:
# 1. Initialize a DP array of size n+1 (where n is the number of rows) with zeros.
# 2. Process the triangle from bottom to top:
#    a. For each element in the current row:
#       i. Update its DP value to be the element's value plus the minimum of the two elements below it.
# 3. After processing all rows, the minimum path sum will be at dp[0].
# 4. Return dp[0].

class Solution:
   def minimumTotal(self, triangle: List[List[int]]) -> int:
       """
       Find the minimum path sum from top to bottom of the triangle.
       
       Args:
           triangle: A list of lists where each inner list represents a row of the triangle
           
       Returns:
           The minimum path sum from top to bottom
       """
       # Get the number of rows in the triangle
       numRows = len(triangle)
       
       # Initialize DP array with one extra element to handle boundary cases
       minPathSums = [0] * (numRows + 1)
       
       # Process the triangle from bottom to top
       for row in reversed(triangle):
           for i, value in enumerate(row):
               # For each element, calculate minimum path sum
               # by choosing the minimum of the two elements below it
               minPathSums[i] = value + min(minPathSums[i], minPathSums[i + 1])
       
       # After processing all rows, minPathSums[0] contains the minimum path sum
       return minPathSums[0]
