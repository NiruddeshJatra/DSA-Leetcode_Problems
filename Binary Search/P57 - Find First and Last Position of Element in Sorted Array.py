# Time Complexity: O(log(n)), where `n` is the length of `nums`.  
# - Each binary search operation runs in O(log(n)) time.  
# - Two binary searches are performed, resulting in O(log(n)) overall.  

# Space Complexity: O(1)  
# - The algorithm uses only a constant amount of extra space.

# INTUITION:  
# The task is to find the starting and ending positions of a target value in a sorted array.  
# Binary search is an optimal approach since the array is sorted.  
# We perform two binary searches:  
# 1. **Find the starting index**:  
#    - We search for the first occurrence of the target by adjusting the `right` pointer when `nums[mid] >= target`.  
# 2. **Find the ending index**:  
#    - We search for the last occurrence of the target by adjusting the `left` pointer when `nums[mid] <= target`.  
# By doing this, we isolate the range where the target appears in O(log(n)) time.

# ALGORITHM:  
# 1. Perform binary search to find the starting index of the target:  
#    - Initialize `left` and `right`.  
#    - Adjust pointers to find the first occurrence of the target.  
# 2. Perform binary search to find the ending index of the target:  
#    - Reinitialize `left` and `right`.  
#    - Adjust pointers to find the last occurrence of the target.  
# 3. If `end` is less than `start`, return `[-1, -1]` as the target is not in the array.  
# 4. Otherwise, return `[start, end]`.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the starting index of the target
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        start = left

        # Find the ending index of the target
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        end = left - 1

        # Check if the target exists in the array
        return [-1, -1] if end < start or start >= len(nums) or nums[start] != target else [start, end]
