# Time Complexity:
# - O(N), where N is the length of the input array
# - We extend the array once and do a single pass through it
# - All operations in the loop are O(1)

# Space Complexity:
# - O(N), where N is the length of the input array
# - We create a new array twice the size of input
# - Could be optimized to O(1) by not creating new array

# INTUITION:
# To find maximum difference between adjacent elements in a circular array:
# 1. The circular nature means first and last elements are adjacent
# 2. We can handle this by extending array with itself
# 3. Then simple linear scan will find max difference between any neighbors
# 4. This includes the "wrap around" difference automatically

# ALGORITHM:
# 1. Extend array by appending itself (handles circular aspect)
# 2. Initialize variable to track maximum difference
# 3. Iterate through array:
#    - Calculate absolute difference between current and previous element
#    - Update maximum difference if current is larger
# 4. Return the maximum difference found

class Solution:
   def maxAdjacentDistance(self, nums: List[int]) -> int:
       extendedArray = nums + nums
       maxDifference = 0
       
       for i in range(1, len(extendedArray)):
           currentDiff = abs(extendedArray[i] - extendedArray[i-1])
           maxDifference = max(maxDifference, currentDiff)
           
       return maxDifference
