# INTUITION:
# The problem requires finding the length of the longest contiguous subarray where the absolute difference 
# between the maximum and minimum elements does not exceed a given `limit`. 
# This suggests a sliding window approach with dynamic size adjustment to maintain the condition:
# - The window expands by adding the current element.
# - The window shrinks from the left whenever the condition (max - min <= limit) is violated.

# To efficiently track the maximum and minimum values in the current window, we use two monotonic deques:
# 1. `maxQ` maintains elements in non-increasing order (front is the largest in the window).
# 2. `minQ` maintains elements in non-decreasing order (front is the smallest in the window).

# ALGORITHM:
# 1. Use two deques (`maxQ` and `minQ`) to track the maximum and minimum elements in the window.
# 2. Iterate through `nums` with the right pointer:
#    - Add the current element to both deques, maintaining their monotonic properties.
#    - If the difference between the maximum and minimum elements exceeds `limit`, shrink the window 
#      from the left by moving the `left` pointer and removing elements from the deques as needed.
# 3. Update the maximum length of the valid subarray (`maxLen`) at each step.
# 4. Return `maxLen` as the result.

# TIME COMPLEXITY:
# O(n), where `n` is the length of `nums`:
# - Each element is added and removed from the deques at most once.

# SPACE COMPLEXITY:
# O(n):
# - Space is used for the two deques, each storing at most `n` elements.

from typing import List
import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Initialize variables
        max_length = 0
        max_deque = collections.deque()  # Tracks maximum elements
        min_deque = collections.deque()  # Tracks minimum elements
        left = 0  # Left pointer of the sliding window
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Update the maximum deque
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            # Update the minimum deque
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            # Check if the current window satisfies the condition
            while max_deque[0] - min_deque[0] > limit:
                # Shrink the window from the left
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            # Update the maximum length of the valid subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length
