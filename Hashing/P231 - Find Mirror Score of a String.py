# Time Complexity:
# - O(N), where N is the length of the input string
#   - We iterate through each character exactly once
#   - Dictionary operations are O(1) on average
# Space Complexity:
# - O(N) in the worst case
#   - The seen dictionary could store up to N/2 positions if no matches are found
# INTUITION:
# The problem requires finding mirrored character pairs and calculating scores based on their positions.
# Using a defaultdict(list) is ideal because:
# 1. It automatically initializes empty lists for new keys, preventing KeyError
# 2. Lists allow us to handle multiple occurrences of the same character
# 3. Using pop() lets us match with the most recent occurrence, which is optimal for minimizing distance
# ALGO:
# 1. Initialize a defaultdict to store positions of characters
# 2. For each character c at position i:
#    - Calculate its mirror character (a->z, b->y, etc.)
#    - If mirror exists in seen, pop latest position and add distance to score
#    - If not, add current character's position to seen
# 3. Return final score
from collections import defaultdict

class Solution:
   def calculateScore(self, s: str) -> int:
       seen = defaultdict(list)
       score = 0
       
       for i, c in enumerate(s):
           mirror = chr(ord('z') - (ord(c) - ord('a')))
           
           if seen[mirror]:
               j = seen[mirror].pop()
               score += (i - j)
           else:
               seen[c].append(i)
               
       return score
