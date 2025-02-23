# Time Complexity:
# - O(N*M*logM) for sorting each row of grid where N is number of rows and M is max columns
# - O(K*logK) for sorting maxArr where K is total count of elements from all rows
# - Overall: O(N*M*logM + K*logK)

# Space Complexity:
# - O(K) for storing maxArr where K is sum of all limits
# - Input grid is modified in-place during sorting

# INTUITION:
# We want to select k largest elements such that we only take specified limit
# of elements from each row. The optimal strategy is to:
# 1. Sort each row in descending order and take top elements based on limit
# 2. Put all these elements in one array and take k largest
#
# Example:
# grid = [[1,2,3], [4,5,6], [7,8,9]]
# limits = [2,1,1]
# k = 3
#
# Step 1: Sort rows -> [[3,2,1], [6,5,4], [9,8,7]]
# Step 2: Take elements based on limits -> [3,2, 6, 9]
# Step 3: Sort and take k largest -> [9,6,3] = 18

# ALGO:
# 1. For each row in grid:
#    - Sort in descending order
#    - Take top elements based on corresponding limit
#    - Add these elements to maxArr
# 2. Sort maxArr in descending order
# 3. Return sum of first k elements

class Solution:
   def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
       # Array to store selected elements
       selectedElements = []
       
       # Process each row
       for rowIndex in range(len(grid)):
           # Sort current row in descending order
           grid[rowIndex].sort(reverse=True)
           
           # Take top elements based on limit
           for colIndex in range(limits[rowIndex]):
               selectedElements.append(grid[rowIndex][colIndex])
       
       # Sort selected elements in descending order
       selectedElements.sort(reverse=True)
       
       # Return sum of k largest elements
       return sum(selectedElements[:k])
