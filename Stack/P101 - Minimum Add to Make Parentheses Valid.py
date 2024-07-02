"""
### Problem
Given a string `s` containing only parentheses `(` and `)`, return the minimum number of parentheses you must add to make the string valid.

### Intuition
A valid parentheses string has matching pairs of opening and closing parentheses in the correct order. To determine the minimum number of parentheses to add, we can use a stack to keep track of unmatched parentheses as we iterate through the string.

### Approach
1. **Initialize Stack**:
   - Use a stack to keep track of unmatched parentheses.
   
2. **Process Each Character**:
   - Iterate through each character in the string `s`.
   - If the stack is not empty and the top of the stack is `(` and the current character is `)`, pop the stack (indicating a valid pair).
   - Otherwise, push the current character onto the stack (indicating an unmatched parenthesis).

3. **Calculate Result**:
   - The size of the stack at the end of the iteration represents the minimum number of parentheses that need to be added to make the string valid.

### Time Complexity
O(n), where n is the length of the string `s`. Each character is processed once.

### Space Complexity
O(n), due to the stack used for unmatched parentheses.

### Code
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)
