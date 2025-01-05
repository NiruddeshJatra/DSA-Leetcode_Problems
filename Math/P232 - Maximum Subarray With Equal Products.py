# Time Complexity:
# - O(N^2 * log M), where N is length of nums array and M is the maximum number in nums
#   - Nested loops: O(N^2) for iterating through all possible subarrays
#   - GCD/LCM calculations: O(log M) for each operation
# Space Complexity:
# - O(1), only using constant extra space for variables
#   - No additional data structures used besides a few variables
# INTUITION:
# To find a valid subarray, we need to check if product = LCM * GCD. By using a two-pointer approach and
# maintaining running calculations of product, LCM and GCD, we can efficiently check all subarrays.
# This works because:
# 1. If product = LCM * GCD, the subarray satisfies the divisibility property
# 2. For each starting index i, we can extend the subarray until the property breaks
# 3. Math.gcd and lcm help efficiently track these values
# ALGO:
# 1. Initialize maxLen to track longest valid subarray found
# 2. For each starting index i:
#    - Initialize product, LCM, and GCD with first number nums[i]
#    - For each ending index j > i:
#      - Update product *= nums[j]
#      - Update LCM = lcm(current_lcm, nums[j])
#      - Update GCD = gcd(current_gcd, nums[j])
#      - If product equals LCM * GCD:
#        - Update maxLen if current length is larger
# 3. Return maxLen
import math
from typing import List

class Solution:
   def maxLength(self, nums: List[int]) -> int:
       def lcm(a, b):
           return (a * b) // math.gcd(a, b)
       
       maxLen = 0
       for i in range(len(nums)):
           curProduct = curLcm = curGcd = nums[i]
           for j in range(i+1, len(nums)):
               curProduct *= nums[j]
               curLcm = lcm(curLcm, nums[j])
               curGcd = math.gcd(curGcd, nums[j])
               if curProduct == curLcm * curGcd:
                   maxLen = max(maxLen, j - i + 1)

       return maxLen
