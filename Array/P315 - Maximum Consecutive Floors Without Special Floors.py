# Time Complexity:
# - O(N log N) where N is length of special array
# - Dominated by sorting the special floors
# - Finding max consecutive is O(N)

# Space Complexity:
# - O(1), only using constant extra space
# - Sorting is typically done in-place

# INTUITION:
# Sort special floors and check gaps between consecutive special floors.
# Don't forget to check gap from bottom to first special floor
# and from last special floor to top floor.
# Maximum consecutive non-special floors will be largest gap minus 1.

# ALGO:
# 1. Sort special floors in ascending order
# 2. Check gap from bottom to first special floor
# 3. Check gaps between consecutive special floors
# 4. Check gap from last special floor to top
# 5. Return maximum gap found

class Solution:
   def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
       special.sort()
       maxConsecutive = special[0] - bottom  # Gap from bottom to first special
       
       # Check gaps between consecutive special floors
       for i in range(1, len(special)):
           currentGap = special[i] - special[i-1] - 1
           maxConsecutive = max(maxConsecutive, currentGap)
           
       # Check gap from last special to top
       maxConsecutive = max(maxConsecutive, top - special[-1])
       
       return maxConsecutive
