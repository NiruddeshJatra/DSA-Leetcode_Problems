# Time Complexity: O(n), where n is the length of the array `nums`. We traverse the array twice, once from the left and once from the right, making the overall complexity linear.
# Space Complexity: O(n), due to the use of two stacks that could potentially store all indices in the worst case.

# INTUITION:
# The goal is to find the shortest subarray that, if sorted, makes the entire array sorted. We need to identify the leftmost and rightmost boundaries of this subarray. 
# 
# **Key Insight**:
# - By using two passes through the array (one from the left and one from the right), we can identify the smallest section of the array that is out of order.
# - The stack helps us track indices where the order is violated.
# - The left pass identifies where elements are greater than a subsequent smaller element (an inversion from sorted order), while the right pass identifies where elements are smaller than a preceding larger element.

# ALGO:
# 1. **Left Pass**:
#    - Initialize `start` to a large value and use a stack to track the left boundary of the unsorted subarray.
#    - Traverse the array from left to right. For each element, if the current element is smaller than the element at the top of the stack, pop from the stack and update the `start` index to the smallest position.
# 2. **Right Pass**:
#    - Initialize `end` to a small value and use a stack to track the right boundary of the unsorted subarray.
#    - Traverse the array from right to left. If the current element is larger than the element at the top of the stack, pop from the stack and update the `end` index to the largest position.
# 3. **Final Check**:
#    - If `start > end`, the array is already sorted, so return 0.
#    - Otherwise, return the length of the unsorted subarray (`end - start + 1`).

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Step 1: Initialize variables
        start, end = len(nums), 0
        stack = []

        # Step 2: Left pass to find the smallest index of the unsorted subarray
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)

        # Step 3: Right pass to find the largest index of the unsorted subarray
        stack = []
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        # Step 4: Final check and return the result
        if start > end:
            return 0
        return end - start + 1
