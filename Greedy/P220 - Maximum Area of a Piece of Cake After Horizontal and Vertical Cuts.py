# Time Complexity:
# - O(H log H + V log V) where H is number of horizontal cuts and V is number of vertical cuts
#   - Sorting horizontal cuts: O(H log H)
#   - Sorting vertical cuts: O(V log V)
#   - Two linear passes through cuts arrays: O(H + V)
#   - Overall dominated by sorting: O(H log H + V log V)

# Space Complexity:
# - O(1), only using primitive variables (maxH, maxW)
#   - The sorts are typically done in-place
#   - No additional data structures created beyond input arrays

# INTUITION:
# To find the largest piece after cuts, we need:
# - Maximum distance between any two adjacent horizontal cuts for height
# - Maximum distance between any two adjacent vertical cuts for width
# By sorting cuts first, we can easily find these maximum gaps
# The product of these maximums will give us the largest possible piece
# We need to handle the edges (0 and h/w) as potential cut points

# ALGO:
# 1. Sort both horizontal and vertical cuts arrays
# 2. Append cake dimensions (h, w) to respective arrays to handle edge cases
# 3. Initialize maxH and maxW with first cuts from 0
# 4. For horizontal cuts:
#    - Find maximum difference between adjacent cuts
# 5. For vertical cuts:
#    - Find maximum difference between adjacent cuts
# 6. Return (maxH * maxW) % (10^9 + 7)

class Solution:
   def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
       # Sort cuts arrays
       horizontalCuts.sort()
       verticalCuts.sort()
       
       # Add cake dimensions to handle edges
       horizontalCuts.append(h)
       verticalCuts.append(w)
       
       # Initialize with first cuts from 0
       maxH, maxW = horizontalCuts[0], verticalCuts[0]
       
       # Find maximum gap between horizontal cuts
       for i in range(1, len(horizontalCuts)):
           maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i-1])
           
       # Find maximum gap between vertical cuts
       for i in range(1, len(verticalCuts)):
           maxW = max(maxW, verticalCuts[i] - verticalCuts[i-1])
           
       # Return product modulo 10^9 + 7
       return (maxH * maxW) % (10**9+7)
