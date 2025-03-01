# Time Complexity:
# - O(m + n), where m and n are the lengths of nums1 and nums2 respectively.
# - We process each element from both arrays exactly once.

# Space Complexity:
# - O(1), as we modify nums1 in-place without using extra space.

# INTUITION:
# Instead of merging from the beginning, we merge from the end to avoid overwriting elements in nums1 that we still need.
# The nums1 array has extra space at the end to accommodate all elements from nums2.
# 
# By starting from the end, we can place the largest elements first, gradually working our way to the smallest ones.
# This approach allows us to avoid using temporary storage for elements that would otherwise be overwritten.
# 
# Think of it like merging two decks of cards, but starting with the highest cards first and working backwards.

# ALGO:
# 1. Start with pointers at the end of the valid portions of both arrays (i at m-1, j at n-1).
# 2. Start filling nums1 from the end (k at m+n-1).
# 3. Compare elements from both arrays and place the larger one at position k in nums1.
# 4. Decrement the appropriate pointers and continue.
# 5. If we've processed all elements from nums1 but still have elements in nums2, copy the remaining nums2 elements to nums1.

class Solution:
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       """
       Merge nums2 into nums1 as one sorted array.
       nums1 has a size of m + n where first m elements are to be merged with n elements from nums2.
       """
       # Initialize pointers: 
       # i points to the last element in nums1's original content
       # j points to the last element in nums2
       # k points to the last position in the final merged array
       leftPointer, rightPointer, mergePointer = m - 1, n - 1, m + n - 1
       
       # Continue until we've processed all elements from nums2
       while rightPointer >= 0:
           # If there are still elements in nums1 and the current nums1 element is larger
           if leftPointer >= 0 and nums1[leftPointer] > nums2[rightPointer]:
               # Place the larger element from nums1 at the current merge position
               nums1[mergePointer] = nums1[leftPointer]
               leftPointer -= 1
           else:
               # Place the current element from nums2 at the current merge position
               nums1[mergePointer] = nums2[rightPointer]
               rightPointer -= 1
           
           # Move to the next merge position
           mergePointer -= 1
           
       # Note: We don't need to handle remaining elements in nums1
       # because they're already in the correct position.
