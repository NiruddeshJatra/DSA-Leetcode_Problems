# INTUITION:
# The problem requires finding the length of the longest subarray of 1's that can be formed if at most one element (0) is removed.
# A sliding window approach is well-suited here because:
# 1. We can maintain a valid window (with at most one 0) and dynamically adjust its size.
# 2. By counting the number of 0's in the current window, we can decide when to shrink the window.

# The sliding window strategy efficiently tracks the number of 1's while skipping or removing at most one 0.
# This avoids checking all possible subarrays (which would be computationally expensive).

# ALGORITHM:
# 1. Initialize variables:
#    - `l`: Left pointer of the sliding window.
#    - `count0`: Tracks the number of 0's in the current window.
#    - `count1`: Tracks the number of 1's in the current window.
#    - `ans`: Stores the maximum length of the subarray with at most one 0 removed.
#
# 2. Expand the window by moving the right pointer `r`:
#    - If the current element is 0, increase `count0`.
#    - If the current element is 1, increase `count1`.
#
# 3. Shrink the window from the left if `count0` exceeds 1:
#    - Adjust `count0` and `count1` based on the element at index `l`.
#    - Move the left pointer `l` forward.
#
# 4. Update `ans` as the maximum length of 1's in the current valid window.
#
# 5. Return the final result:
#    - If the entire array consists of 1's, the result should be `len(nums) - 1` since removing one 1 is mandatory.

# TIME COMPLEXITY:
# O(n), where `n` is the length of `nums`:
# - The right pointer traverses the array once.
# - The left pointer only moves forward, so the shrinking of the window is O(n) in total.

# SPACE COMPLEXITY:
# O(1):
# - The solution uses a constant amount of additional space.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Variables to track the result and the window boundaries
        max_length = 0
        left = 0
        
        # Variables to track the counts of 0's and 1's in the window
        zero_count = 0
        one_count = 0
        
        # Traverse the array with the right pointer
        for right in range(len(nums)):
            # Update the counts based on the current element
            if nums[right] == 0:
                zero_count += 1
            else:
                one_count += 1
            
            # Shrink the window if more than one 0 is present
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                else:
                    one_count -= 1
                left += 1
            
            # Update the maximum length of valid subarray
            max_length = max(max_length, one_count)
        
        # Handle the case where the array contains only 1's
        return max_length if max_length != len(nums) else max_length - 1
