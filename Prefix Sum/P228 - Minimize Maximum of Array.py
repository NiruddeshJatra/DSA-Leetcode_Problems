# Time Complexity:
# - O(N) where N is length of array
#   - Single pass to calculate sum and max value

# Space Complexity:
# - O(1), using only variables s and ans

# INTUITION:
# To minimize maximum value after operations:
# - Can only move values left
# - Running average is minimum possible value 
# - Need to track maximum running average
# This reveals optimal strategy is leveling elements

# ALGO:
# 1. Track running sum and index for average
# 2. For each number:
#    - Add to running sum
#    - Update max with ceil(sum/(i+1))
# 3. Return maximum found

class Solution:
   def minimizeArrayValue(self, nums: List[int]) -> int:
       # Initialize sum and result
       ans = s = 0
       
       # Calculate max running average
       for i in range(len(nums)):
           s += nums[i]
           ans = max(ans, (s+i)//(i+1))
           
       return ans
