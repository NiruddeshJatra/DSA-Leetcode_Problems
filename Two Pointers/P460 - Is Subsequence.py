# Time Complexity:
# - O(|t| + |s| * log|t|), where |s| and |t| are lengths of strings s and t
# - O(|t|) to build the index map for string t
# - O(|s| * log|t|) for binary search operations on each character in s

# Space Complexity:
# - O(|t|) to store the index mapping for all characters in string t
# - Each character's indices are stored in separate lists

# INTUITION:
# The problem asks if string s is a subsequence of string t
# A subsequence maintains relative order but allows gaps between characters
# Key strategy:
# - Preprocess string t to create an index map for each character
# - For each character in s, find the next valid position in t using binary search
# - This ensures we maintain the sequential order requirement
# Example:
# s = "ace", t = "aebdc"
# Index map: {'a': [0], 'e': [1], 'b': [2], 'd': [3], 'c': [4]}
# For 'a': find index >= 0 → found at 0, next search starts at 1
# For 'c': find index >= 1 → not found in 'c' indices, but we need 'e' first
# For 'e': find index >= 1 → found at 1, next search starts at 2

# ALGO:
# 1. Build an index map storing all positions of each character in string t
# 2. Initialize nextIndex to track the minimum position for next character
# 3. For each character in s:
#    - Use binary search to find the next valid index in t
#    - Update nextIndex to ensure subsequent characters appear after current one
#    - If no valid index is found, return False
# 4. Return True if all characters in s are successfully matched

class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
       # Build index map for all characters in string t
       charIndexMap = defaultdict(list)
       for index, char in enumerate(t):
           charIndexMap[char].append(index)
       
       def findNextValidIndex(indexList, minStartIndex):
           # Use binary search to find the first index >= minStartIndex
           insertPosition = bisect_left(indexList, minStartIndex)
           
           # If no valid index found, return -1
           if insertPosition == len(indexList):
               return -1
               
           # Return the next index after the found position
           return indexList[insertPosition] + 1
       
       # Track the minimum index for the next character search
       nextSearchIndex = 0
       
       # Process each character in string s
       for currentChar in s:
           # Check if we've exhausted all positions in t
           if nextSearchIndex > len(t):
               return False
           
           # Find the next valid index for current character
           nextSearchIndex = findNextValidIndex(charIndexMap[currentChar], nextSearchIndex)
           
           # If no valid position found, subsequence is impossible
           if nextSearchIndex == -1:
               return False
       
       # All characters in s were successfully matched
       return True
