"""
### Problem
Given a collection of intervals, merge all overlapping intervals and return an array of the merged intervals.

### Intuition
To merge overlapping intervals, we can sort the intervals based on their starting points. Then, by iterating through the sorted intervals, we can merge them by checking if the current interval overlaps with the previous one.

### Approach
1. **Sort Intervals**:
   - Sort the intervals by their starting points.

2. **Initialize Stack**:
   - Use a stack to store merged intervals.
   
3. **Process Each Interval**:
   - Iterate through the sorted intervals.
   - For each interval, check if it overlaps with the interval on top of the stack.
   - If it overlaps, merge the intervals by updating the start and end points.
   - If it does not overlap, push the interval onto the stack.

4. **Return Result**:
   - The stack will contain the merged intervals.

### Time Complexity
O(n log n) for sorting the intervals and O(n) for merging them, where n is the number of intervals.

### Space Complexity
O(n), where n is the number of intervals, due to the stack used for storing merged intervals.

### Code
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their starting points
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # Initialize an empty stack
        stack = []
        
        # Iterate through each interval
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            
            # Check for overlap with the interval on top of the stack
            while stack and stack[-1][1] >= intervals[i][0]:
                start, end = min(stack[-1][0], intervals[i][0]), max(stack[-1][1], intervals[i][1])
                stack.pop()
            
            # Push the merged interval onto the stack
            stack.append([start, end])
        
        # Return the stack containing merged intervals
        return stack
