# Time Complexity: O(n), where n is the length of the string s. 
# We traverse the string once, and each operation with the stack is O(1).

# Space Complexity: O(n) in the worst case, where all characters are '(' and stored in the stack.

# INTUITION:
# The idea is to use a stack to keep track of the current depth of parentheses. 
# Each time we encounter an opening parenthesis '(', we push it onto the stack 
# and check if the current depth is greater than the maximum depth recorded so far.

# ALGO:
# 1. Initialize a variable `ans` to store the maximum depth and an empty stack.
# 2. Iterate through each character in the string:
#    2.1 If the character is '(', push it onto the stack and update `ans` 
#         to be the maximum of its current value and the length of the stack.
#    2.2 If the character is ')', pop the top element from the stack.
# 3. Return the maximum depth recorded in `ans`.

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                ans = max(ans, len(stack))
            elif c == ')':
                stack.pop()
        return ans
