# Time Complexity:
# - O(N), where N is length of nums array
# - Single pass through the array

# Space Complexity:
# - O(1), not counting output array
# - Modifies input array in-place to track seen numbers

# INTUITION:
# Use array elements as indices and mark visited numbers
# by making them negative. If we encounter a negative number
# at an index, that number has been seen before.
# This works because array contains nums from 1 to n.

# ALGO:
# 1. Initialize empty result array for duplicates
# 2. For each number in array:
#    - Take absolute value as index (num - 1)
#    - If number at that index is negative:
#      - We've seen this number before, add to duplicates
#    - Mark as seen by making number negative
# 3. Return array of duplicates

class Solution:
   def findDuplicates(self, nums: List[int]) -> List[int]:
       duplicateNums = []
       
       for num in nums:
           currentNum = abs(num)  # Get positive value
           targetIndex = currentNum - 1
           
           # If already negative, we've seen this number
           if nums[targetIndex] < 0:
               duplicateNums.append(currentNum)
               
           # Mark as seen by making negative    
           nums[targetIndex] *= -1
           
       return duplicateNums
