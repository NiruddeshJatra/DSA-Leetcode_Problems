# Time Complexity:
# - O(N) where N is length of string
# - Single pass through string using two pointers
# - Each character is processed exactly once

# Space Complexity:
# - O(1) as we only use a few variables
# - No additional space needed relative to input size

# INTUITION:
# A homogenous substring contains same character repeated
# For each character position, we can count how many
# homogenous substrings end at that position
# Example: "abbccc"
# At 'a': ["a"] = 1
# At first 'b': ["b"] = 1
# At second 'b': ["b", "bb"] = 2
# At first 'c': ["c"] = 1
# At second 'c': ["c", "cc"] = 2
# At third 'c': ["c", "cc", "ccc"] = 3
# Total = 10

# ALGO:
# 1. Use two pointers: left marks start of current homogenous sequence
# 2. For each character (right pointer):
#    - If same as char at left:
#      Add number of substrings ending at right
#      (right-left+1 new substrings possible)
#    - If different:
#      Add 1 (just single char substring)
#      Update left to start new sequence
# 3. Return count modulo 10^9 + 7

def countHomogenous(self, s: str) -> int:
   MOD = 10**9 + 7
   leftPointer = 0
   totalCount = 0
   
   for rightPointer in range(len(s)):
       if s[leftPointer] == s[rightPointer]:
           # Add count of all substrings ending at rightPointer
           # Length of current sequence is (right-left+1)
           totalCount += rightPointer - leftPointer + 1
       else:
           # Different character found
           # Add 1 for single character substring
           totalCount += 1
           # Start new sequence
           leftPointer = rightPointer
           
   return totalCount % MOD
