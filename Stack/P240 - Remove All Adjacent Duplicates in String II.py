# Time Complexity:
# - O(N), where N is length of string s
#   - We iterate through string once
#   - Stack operations (append/pop) are O(1)
#   - Final string construction takes O(N) in worst case
# Space Complexity:
# - O(N) for the stack
#   - Stack stores character-count pairs
#   - In worst case (no duplicates/removals), stores N pairs
# INTUITION:
# Using a stack with [char, count] pairs is efficient because:
# 1. Stack naturally tracks consecutive characters
# 2. Can quickly check/update count of current character
# 3. Pop operation handles removal of k duplicates
# 4. Final string construction is straightforward
# ALGO:
# 1. Initialize empty stack to store [character, count] pairs
# 2. For each character in string:
#    - If stack not empty and current char matches top char:
#      - Increment count at top of stack
#      - If count reaches k, pop the pair
#    - Else:
#      - Push new pair [char, 1] to stack
# 3. Build final string:
#    - For each [char, count] in stack
#    - Append char repeated count times
# 4. Return result string
from typing import List

class Solution:
   def removeDuplicates(self, s: str, k: int) -> str:
       # Stack stores [character, frequency] pairs
       charStack = []
       
       # Process each character
       for char in s:
           if charStack and char == charStack[-1][0]:
               # Increment count of consecutive char
               charStack[-1][1] += 1
               # Remove if k consecutive found
               if charStack[-1][1] == k:
                   charStack.pop()
           else:
               # Start new character sequence
               charStack.append([char, 1])
       
       # Construct result string
       result = ''
       for char, count in charStack:
           result += char * count
           
       return result
