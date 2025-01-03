# Time Complexity:
# - O(N^2) where N is string length
# - String reversal can take O(N) for each nested parenthesis

# Space Complexity:
# - O(N) for stack and current string storage

# INTUITION:
# Process string left to right:
# - Build current string until '(' found
# - Save current string on stack at '('
# - At ')', reverse current and combine with stack top

# ALGO:
# 1. Initialize stack and current string
# 2. For each character:
#    - '(': push current to stack, reset current
#    - ')': reverse current, combine with stack top
#    - else: add to current string
# 3. Return final string

class Solution:
   def reverseParentheses(self, s: str) -> str:
       stack = []
       curStr = ''
       
       for c in s:
           if c == '(':
               stack.append(curStr)
               curStr = ''
           elif c == ')':
               curStr = stack.pop() + curStr[::-1]
           else:
               curStr += c
               
       return curStr
