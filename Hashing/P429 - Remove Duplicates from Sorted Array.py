# Time Complexity:
# - O(N), where N is the length of the array.
# - We only iterate through the array once, processing each element in constant time.

# Space Complexity:
# - O(1), as we modify the array in-place without using any extra space that scales with input size.

# INTUITION:
# This problem is asking us to remove duplicates from a sorted array such that each element appears at most twice,
# and return the new length of the modified array.
#
# The key insight is to maintain a pointer (k) that points to the position where the next valid element should be placed.
# Initially, we keep the first two elements as they are (since we allow up to two occurrences).
# Then, for each subsequent element, we check if it's different from the element at position k-1.
#
# If it's different, it means we haven't seen this element twice yet, so we can include it.
# If it's the same, it means we already have two occurrences of this element, so we skip it.
#
# For example, with nums = [1,1,2,2,3]:
# - k starts at 1 (we keep nums[0]=1)
# - For nums[2]=1: since nums[2]=1 equals nums[k-2]=1, we skip it
# - For nums[3]=2: since nums[3]=2 doesn't equal nums[k-2]=1, we place it at nums[k=2] and increment k to 3
# - For nums[4]=2: since nums[4]=2 doesn't equal nums[k-2]=1, we place it at nums[k=3] and increment k to 4
# - For nums[5]=3: since nums[5]=3 doesn't equal nums[k-2]=2, we place it at nums[k=4] and increment k to 5
# The final array is [1,2,3,...] with length 3.

# ALGO:
# 1. If the array has less than or equal to 1 elements, return the length of the array (all elements are valid).
# 2. Initialize a pointer k to 2 (as we keep the first two elements as they are).
# 3. Iterate through the array starting from index 1:
#    a. If the current element is different from the element at position k-1:
#       i. Place the current element at position k.
#       ii. Increment k.
# 4. Return k, which represents the new length of the modified array.

from typing import List

class Solution:
   def removeDuplicates(self, nums: List[int]) -> int:
       # Handle edge cases
       if len(nums) <= 1:
           return len(nums)
       
       # Initialize pointer to track position for next valid element
       # Start at 2 because we always keep the first two elements
       validPosition = 1
       
       # Process each element starting from the third element
       for i in range(1, len(nums)):
           # If the current element is different from the element at validPosition-2,
           # it means we haven't seen this element twice yet
           if nums[i] != nums[validPosition-1]:
               # Place the current element at the validPosition
               nums[validPosition] = nums[i]
               # Move the validPosition pointer forward
               validPosition += 1
       
       # Return the new length of the modified array
       return validPosition
