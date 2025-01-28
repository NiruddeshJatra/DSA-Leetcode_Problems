# Time Complexity:
# - O(N), where N is the length of nums array
# - Single pass through the array, swapping adjacent elements when needed

# Space Complexity:
# - O(1), only uses constant extra space
# - Array is modified in place

# INTUITION:
# Traverse array and ensure alternating pattern by swapping adjacent elements
# when they violate the desired ordering:
# - Even indices should have larger elements than odd indices
# - Odd indices should have smaller elements than even indices

# ALGO:
# 1. Iterate through array from start to second-last element
# 2. For odd indices: swap if current > next
# 3. For even indices: swap if current < next
# 4. Return modified array

class Solution:
   def rearrangeArray(self, nums: List[int]) -> List[int]:
       for currentIndex in range(len(nums) - 1):
           # If odd index and current < next OR even index and current > next
           shouldSwap = ((currentIndex % 2 and nums[currentIndex] < nums[currentIndex + 1]) or 
                        (not currentIndex % 2 and nums[currentIndex] > nums[currentIndex + 1]))
           
           if shouldSwap:
               nums[currentIndex], nums[currentIndex + 1] = nums[currentIndex + 1], nums[currentIndex]

       return nums
