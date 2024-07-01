"""
### Problem
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

### Intuition
To solve this problem, we can use a histogram-based approach. For each row in the matrix, we treat the row as the base of a histogram where the height of each column is the number of consecutive 1's ending in that column. Using a stack, we can efficiently compute the largest rectangle for each histogram.

### Approach
1. **Initialize Variables**:
   - `heights` to store the histogram heights for each column.
   - `maxArea` to keep track of the maximum area found.

2. **Update Heights**:
   - For each row, update the `heights` array. If the current cell is '1', increment the height; otherwise, reset the height to 0.

3. **Compute Maximum Area for Histogram**:
   - Use a stack to compute the largest rectangle area for the current histogram.
   - For each height, pop from the stack until the current height is greater than the height at the stack's top index. Calculate the width using `i if not stack else i - stack[-1] - 1` and update `maxArea`.

### Time Complexity
O(n * m), where n is the number of rows and m is the number of columns. Each element is processed once for height update and once for area computation.

### Space Complexity
O(m), where m is the number of columns, due to the additional height and stack storage.

### Code
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * (len(matrix[0]) + 1)
        maxArea = 0
        
        for row in matrix:
            for i in range(len(matrix[0])):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    index = stack.pop()
                    height = heights[index]
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, height * width)
                stack.append(i)
        
        return maxArea
