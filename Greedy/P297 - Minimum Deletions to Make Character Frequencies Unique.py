# Time Complexity: O(N)
# Space Complexity: O(1) as freq will have max 26 letters

# INTUITION:
# Reduce frequencies to ensure unique frequency distribution
# Decrement frequencies with conflicts until all unique

class Solution:
   def minDeletions(self, s: str) -> int:
       freq = Counter(s)
       deletions = 0
       usedFrequencies = set()

       for char, count in freq.items():
           while count and count in usedFrequencies:
               count -= 1
               deletions += 1
           
           if count:
               usedFrequencies.add(count)

       return deletions
