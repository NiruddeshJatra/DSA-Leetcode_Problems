# Time Complexity:
# - O(N) where N is length of string
# - Each character is only considered once as we move l pointer
# - Inner while loop is bounded by k

# Space Complexity:
# - O(1) as we only use a few variables
# - No additional data structures needed

# INTUITION:
# We're looking for exactly k consecutive same characters that aren't part of a longer sequence.
# Use two pointers to find runs of same character:
# - l points to start of potential sequence
# - r counts length of consecutive same chars from l
# Skip if current char continues previous sequence
# Example: s = "aaabba", k = 2
# - l=0: "aaa" (r=3) - skip, too long
# - l=3: "bb" (r=2) - valid! exactly k=2
# Key insight: Only need to check sequences starting at new character

# ALGO:
# 1. For each position l in string:
#    - Skip if it continues previous sequence (same as s[l-1])
#    - Count consecutive same chars (r) from position l
#    - If count equals k and next char different (or end of string)
#      * Found valid sequence
#    - Move l forward by r to skip processed chars
# 2. Return false if no valid sequence found

from typing import List

class Solution:
   def hasSpecialSubstring(self, string: str, targetLength: int) -> bool:
       currentPosition = 0
       stringLength = len(string)
       
       # Process each position in string
       while currentPosition < stringLength:
           # Skip if this continues previous sequence
           if currentPosition > 0 and string[currentPosition] == string[currentPosition - 1]:
               currentPosition += 1
               continue
           
           # Count consecutive same characters
           runLength = 0
           while (currentPosition + runLength < stringLength and 
                  runLength < targetLength and 
                  string[currentPosition] == string[currentPosition + runLength]):
               runLength += 1
           
           # Check if we found valid sequence
           if (runLength == targetLength and 
               (currentPosition + runLength >= stringLength or 
                string[currentPosition] != string[currentPosition + runLength])):
               return True
           
           # Skip processed characters
           currentPosition += runLength
       
       return False
