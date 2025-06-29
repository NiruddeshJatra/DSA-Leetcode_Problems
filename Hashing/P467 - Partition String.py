# Time Complexity:
# - O(n), where n is the length of the input string
# - We iterate through the string once
# - String concatenation and hash map operations are amortized O(1)

# Space Complexity:
# - O(n) to store the frequency map and the current segment being built
# - In the worst case, we might store all unique substrings

# INTUITION:
# The problem asks to partition a string into the minimum number of substrings
# such that each substring contains at most one occurrence of each character
# Key strategy:
# - Build segments character by character
# - When we encounter a character that would create a duplicate in current segment,
#   we finalize the current segment and start a new one
# - Use a frequency map to track which segments we've already created
# Example:
# s = "abacaba"
# First segment: "aba" (contains duplicate 'a', so we stop at "ab")
# Actually: "a", then "b", then we'd get duplicate 'a', so segment = "ab"
# Continue building until we have minimum partitions

# ALGO:
# 1. Initialize empty frequency map and empty current segment
# 2. For each character in the string:
#    - Add character to current segment
#    - Check if current segment has been seen before
#    - If not seen, add to frequency map and start new segment
#    - If seen, continue building current segment
# 3. Return all unique segments found

class Solution:
   def partitionString(self, s: str) -> List[str]:
       # Track unique segments we've created
       uniqueSegments = {}
       currentSegment = ""
       
       # Process each character in the string
       for char in s:
           # Add current character to the segment being built
           currentSegment += char
           
           # If this segment hasn't been seen before, finalize it
           if currentSegment not in uniqueSegments:
               uniqueSegments[currentSegment] = 1
               currentSegment = ""  # Start building a new segment
       
       # Return all unique segments created
       return list(uniqueSegments.keys())
