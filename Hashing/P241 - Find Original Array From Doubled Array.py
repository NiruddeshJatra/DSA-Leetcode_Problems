# Time Complexity:
# - O(N log N), where N is length of changed array
#   - Sorting frequencies takes O(K log K) where K is number of unique elements
#   - Processing each element takes O(N) total
# Space Complexity:
# - O(N) for Counter dictionary
#   - Stores frequency of each number
#   - Result array also takes O(N) space
# INTUITION:
# For array to be valid doubled array:
# 1. Each number x must have frequency ≤ frequency of 2x
# 2. Zero frequency must be even (forms its own pairs)
# 3. Processing in sorted order ensures prerequisites are checked first
# Using Counter makes frequency tracking efficient
# ALGO:
# 1. Create frequency counter for all numbers
# 2. Check if zeros can be paired (frequency must be even)
# 3. For each number n in sorted order:
#    - If freq(n) > freq(2n): impossible, return []
#    - Subtract freq(n) from freq(2n)
#    - Handle zeros specially by pairing with themselves
# 4. Return remaining numbers using Counter.elements()
from typing import List
from collections import Counter

class Solution:
   def findOriginalArray(self, changed: List[int]) -> List[int]:
       # Count frequencies
       frequencies = Counter(changed)
       
       # Check if zeros can be paired
       if frequencies[0] % 2:
           return []
       
       # Process numbers in sorted order
       for num in sorted(frequencies):
           # Check if number can be paired with its double
           if frequencies[num] > frequencies[num * 2]:
               return []
           
           # Subtract pairs from double's frequency
           if num == 0:
               frequencies[0] //= 2  # Handle zeros specially
           else:
               frequencies[num * 2] -= frequencies[num]
               
       # Return original array elements
       return list(frequencies.elements())
