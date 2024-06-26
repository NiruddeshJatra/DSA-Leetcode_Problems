"""
### Problem
Given an array of integers `heights` representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed within the bounds of the histogram.

### Intuition
To find the largest rectangle in a histogram, a stack can be used to keep track of the heights and their positions. By maintaining the stack, we can efficiently calculate the maximum area for each bar by determining the left and right boundaries where the bar can extend.

### Approach
1. **Initialize Variables**: Start with `maxArea` to keep track of the maximum area found and an empty `stack` to store pairs of (index, height).
2. **Iterate Through Heights**: For each bar in the histogram, adjust the stack to maintain the order of heights:
   - If the current height is less than the height of the bar on top of the stack, calculate the area with the height of the bar from the stack.
   - Pop the stack until the current bar's height is greater than the height of the bar from the stack, updating the `maxArea` each time.
   - Push the current bar's index and height onto the stack.
3. **Final Calculation**: After processing all bars, there may be bars left in the stack. Calculate the area for these bars as if they extend to the end of the histogram.
4. **Return Result**: Return the `maxArea` found.

### Time Complexity
The time complexity is O(n) where n is the number of bars in the histogram. Each bar is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack.

### Code
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  # Initialize maxArea to keep track of the maximum area found
        stack = []  # Stack to store pairs of (index, height)
        
        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i
            # Adjust the stack to maintain the order of heights
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            # Push the current bar's index and height onto the stack
            stack.append([start, h])
        
        # Final calculation for bars left in the stack
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        
        # Return the maximum area found
        return maxArea
