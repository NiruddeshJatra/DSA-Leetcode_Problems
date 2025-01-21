# Time Complexity:
# - O(N) where N is the length of input strings
# - We iterate through both strings once using zip()

# Space Complexity:
# - O(1) as we only use two variables to store counts
# - No extra space that grows with input size

# INTUITION:
# The key observation is that we can have two types of mismatches:
# 1. 'x' in s1 and 'y' in s2 (xy pair)
# 2. 'y' in s1 and 'x' in s2 (yx pair)
# For xy pairs, we need 1 swap to match 2 positions
# For xy+yx odd pairs, it's impossible to match all positions
# For odd number of xy (or yx), we need an extra swap

# ALGO:
# 1. Count mismatched pairs:
#    - Count xy pairs (x in s1, y in s2)
#    - Count yx pairs (y in s1, x in s2)
# 2. If total mismatches (xy + yx) is odd, return -1 as it's impossible
# 3. If xy count is odd:
#    - Need (xy + yx)/2 + 1 swaps
# 4. If xy count is even:
#    - Need (xy + yx)/2 swaps

class Solution:
   def minimumSwap(self, firstString: str, secondString: str) -> int:
       xyCount = 0  # Count of 'x' in s1 matched with 'y' in s2
       yxCount = 0  # Count of 'y' in s1 matched with 'x' in s2
       
       # Count mismatched pairs
       for char1, char2 in zip(firstString, secondString):
           if char1 != char2:
               if char1 == 'x':
                   xyCount += 1
               else:
                   yxCount += 1
       
       totalMismatches = xyCount + yxCount
       
       # If total mismatches is odd, impossible to match all
       if totalMismatches % 2:
           return -1
           
       # If xy count is odd, need an extra swap
       if xyCount % 2:
           return totalMismatches // 2 + 1
           
       # If xy count is even
       return totalMismatches // 2
