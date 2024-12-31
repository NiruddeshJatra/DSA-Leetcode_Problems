# Time Complexity:
# - O(N) where N is length of input string
#   - Single pass through string: O(N)
#   - Each character is pushed/popped at most once
#   - Final join operation: O(N)

# Space Complexity:
# - O(N) where N is length of input string
#   - Stack can grow up to size N in worst case
#   - No other significant space usage

# INTUITION:
# This is a stack problem because:
# - '*' removes previous character (LIFO behavior)
# - Need to track characters that can be removed
# - Stack naturally handles removal of most recent element
# We can process string left to right, using stack to
# maintain characters that haven't been removed by stars

# ALGO:
# 1. Initialize empty stack
# 2. For each character in string:
#    - If character is '*':
#      * Pop from stack if not empty
#    - Else:
#      * Add character to stack
# 3. Join remaining characters in stack
# 4. Return resulting string

class Solution:
   def removeStars(self, s: str) -> str:
       # Initialize stack for characters
       stack = []
       
       # Process each character
       for c in s:
           if c == '*':
               # Remove previous character if exists
               if stack:
                   stack.pop()
           else:
               # Add non-star character
               stack.append(c)
       
       # Join remaining characters
       return ''.join(stack)
