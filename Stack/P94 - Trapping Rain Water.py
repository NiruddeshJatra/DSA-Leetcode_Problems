"""
### Problem
Given a list of non-negative integers `height` representing the height of bars, compute how much water it can trap after raining.

### Intuition
The water trapped depends on the height of bars to the left and right of each bar. To efficiently calculate the water trapped, we can use a stack to keep track of the bars and calculate the water trapped when we find a bar that is higher than the bar at the top of the stack.

### Approach
1. **Initialize Variables**:
   - `stack`: A stack to keep track of the indices of the bars.
   - `water`: A variable to accumulate the total amount of water trapped.
2. **Iterate Through Bars**:
   - For each bar, check if it is higher than the bar at the top of the stack.
   - If it is, calculate the water trapped between the current bar and the bar at the new top of the stack after popping. The trapped water depends on the height difference between the current bar, the popped bar, and the new top bar.
   - Push the current bar index onto the stack.
3. **Return Result**: The accumulated water is the total amount of water trapped.

### Time Complexity
The time complexity is O(n) where n is the number of bars. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack.

### Code
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # Stack to keep track of bar indices
        water = 0   # Total water trapped
        
        for right in range(len(height)):
            # Process the stack while the current bar is taller than the bar at the stack's top
            while stack and height[stack[-1]] < height[right]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                # Calculate the trapped water using the min height of left and right bars minus the middle bar height
                minHeight = min(height[right], height[left]) - height[mid]
                width = right - left - 1  # Width of the trapped water area
                water += minHeight * width
            # Push the current bar index onto the stack
            stack.append(right)
        
        return water
