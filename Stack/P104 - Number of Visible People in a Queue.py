"""
### Problem
Given an array `heights` representing the heights of people standing in a line, return an array `answer` such that `answer[i]` is the number of people `heights[i]` can see to their right.

### Intuition
The problem involves determining how many people a person can see to their right, where a taller person blocks the view of shorter people behind them. Using a stack can help efficiently track and count visible people.

### Approach
1. **Initialize Stack and Answer List**:
   - Use a stack to keep track of indices of heights.
   - Initialize the `ans` list with zeros, where `ans[i]` will store the number of people `heights[i]` can see.
2. **Iterate from Right to Left**:
   - Start from the rightmost person and move to the left.
   - For each person, count the number of people they can see by popping from the stack until a taller person is found.
   - Update the count accordingly and push the current person's index to the stack.
3. **Return the Result**:
   - After iterating through all people, return the `ans` list which contains the count of visible people for each person in the line.

### Time Complexity
O(n), where n is the length of the `heights` list. Each element is processed once with stack operations being amortized O(1).

### Space Complexity
O(n), due to the stack used for maintaining the indices.

### Code
"""

from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            count = 0
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            ans[i] = count
            stack.append(i)
        
        return ans
