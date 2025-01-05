# Time Complexity:
# - O(N + M), where N is length of string s and M is length of pattern p
#   - str.find() method takes O(N) time in Python
#   - We perform two find operations
# Space Complexity:
# - O(1), only using constant extra space for index variables
#   - No additional data structures are created
# INTUITION:
# When matching a pattern with a single asterisk, we can split the problem into two parts:
# 1. Finding the prefix (everything before the asterisk) in the string
# 2. Finding the suffix (everything after the asterisk) in the remaining substring
# This works because:
# - The asterisk matches any sequence of characters
# - We only need to verify that prefix and suffix exist in the correct order
# ALGO:
# 1. Find the position of asterisk in pattern
# 2. Search for prefix (pattern before asterisk) in main string
#    - If not found, return False
# 3. Search for suffix (pattern after asterisk) in remaining substring
#    - If not found, return False
# 4. Return True if both prefix and suffix are found in correct order
from typing import List

class Solution:
   def hasMatch(self, s: str, p: str) -> bool:
       # Find asterisk position in pattern
       asteriskPos = p.find('*')
       
       # Find prefix match position
       prefixPattern = p[:asteriskPos]
       prefixPos = s.find(prefixPattern)
       if prefixPos == -1:
           return False
           
       # Find suffix in remaining string
       suffixPattern = p[asteriskPos + 1:]
       remainingStr = s[prefixPos + asteriskPos:]
       if remainingStr.find(suffixPattern) == -1:
           return False
           
       return True
