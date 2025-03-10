# Time Complexity:
# - O(N), where N is the length of the input array.
# - In the worst case, we might need to scan through all elements once.
# - The count() method at the end also takes O(N) time.

# Space Complexity:
# - O(1), as we only use a constant amount of extra space regardless of input size.
# - The algorithm performs the operation in-place by swapping elements.

# INTUITION:
# The goal is to remove all occurrences of a specific value from an array. Instead of actually
# removing elements (which would require shifting), we can move all non-target values to the front
# of the array. This is done by using a two-pointer approach:
#
# For example, if nums = [3,2,2,3] and val = 3:
# 1. Start with i=0, find first non-val element at k=1 (value 2), swap nums[0] and nums[1]
# 2. Array becomes [2,3,2,3], increment i to 1
# 3. Find next non-val element at k=2 (value 2), swap nums[1] and nums[2]
# 4. Array becomes [2,2,3,3], increment i to 2
# 5. No more non-val elements, so break
# 6. The first 2 elements are non-val elements, which matches our return value

# ALGO:
# 1. Initialize a pointer i at 0, which tracks the position for the next non-val element.
# 2. For each position i, find the next non-val element (if any) using pointer k.
# 3. If a non-val element is found, swap it with the element at position i and increment i.
# 4. If no more non-val elements are found, break the loop.
# 5. Return the count of elements that aren't equal to val.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Check for empty array edge case
        if not nums:
            return 0
            
        # Position where we'll place the next non-val element
        nextPosition = 0
        
        for i in range(len(nums)):
            # If current element is not the value to be removed
            if nums[i] != val:
                # Move it to the next position in our result
                nums[nextPosition] = nums[i]
                nextPosition += 1
                
        return nextPosition
        
    # Alternative implementation that follows the original approach
    def removeElement_original(self, nums: List[int], val: int) -> int:
        i = 0  # Position for the next non-val element
        
        while i < len(nums):
            # Find the next non-val element
            k = i
            while k < len(nums) and nums[k] == val:
                k += 1
                
            # If we've reached the end of the array, we're done
            if k == len(nums):
                break
                
            # Swap the non-val element to position i
            nums[i], nums[k] = nums[k], nums[i]
            i += 1  # Move to next position
        
        # Return the count of elements that aren't equal to val
        return i  # Alternative to using len(nums) - nums.count(val)
