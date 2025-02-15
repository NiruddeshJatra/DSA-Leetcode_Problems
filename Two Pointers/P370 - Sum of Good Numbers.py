# Time Complexity:
# - O(N) where N is length of array
# - For each number, we check at most 2 other positions (left and right at distance k)

# Space Complexity:
# - O(1) as we only use a few variables
# - No additional data structures needed

# INTUITION:
# A number is "good" if it's strictly greater than its neighbors at distance k.
# We check left and right neighbors at distance k for each position.
# Key insight: Just need to compare with neighbors at exactly distance k.
# Example: nums = [3,6,2,5,3], k = 2
# For nums[1] = 6:
# - Left at i-k = -1 (out of bounds, so valid)
# - Right at i+k = 3, nums[3] = 5 (6 > 5, so valid)
# 6 is a good number

# ALGO:
# 1. For each index i in array:
#    - Calculate left index (i-k) and right index (i+k)
#    - Check if current number is greater than both neighbors
#    - If left exists and current ≤ left, not good
#    - If right exists and current ≤ right, not good
#    - If good, add to total
# 2. Return sum of all good numbers

from typing import List

class Solution:
   def sumOfGoodNumbers(self, nums: List[int], distance: int) -> int:
       totalSum = 0
       arrayLength = len(nums)
       
       # Check each number in array
       for currentIndex in range(arrayLength):
           # Calculate indices at distance k
           leftIndex = currentIndex - distance
           rightIndex = currentIndex + distance
           
           isGoodNumber = True
           
           # Check left neighbor if it exists
           if leftIndex >= 0 and nums[currentIndex] <= nums[leftIndex]:
               isGoodNumber = False
           
           # Check right neighbor if it exists
           if rightIndex < arrayLength and nums[currentIndex] <= nums[rightIndex]:
               isGoodNumber = False
           
           # Add to sum if number is good
           if isGoodNumber:
               totalSum += nums[currentIndex]
       
       return totalSum
