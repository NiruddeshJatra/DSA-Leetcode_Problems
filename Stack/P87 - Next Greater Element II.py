"""
### Problem
Given a circular array `nums`, find the next greater number for every element in `nums`. The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

### Intuition
To solve this problem, we can extend the array by concatenating it with itself, thus transforming the circular nature into a linear one. This allows us to reuse the approach of finding the next greater element using a stack.

### Approach
1. **Extend the Array**: Concatenate the array `nums` with itself to handle the circular nature.
2. **Initialize Data Structures**: Create a list `ans` initialized to -1 of the same length as the extended array. Initialize an empty stack to keep track of indices for which we need to find the next greater element.
3. **Iterate Through the Extended Array**: Loop through each element in the extended array:
   - While the stack is not empty and the current element is greater than the element at the index on the top of the stack:
     - Pop the index from the stack.
     - Update the next greater element for the popped index in `ans`.
   - Push the current index onto the stack.
4. **Return the Result**: Return the first half of the `ans` list, which corresponds to the original length of `nums`.

### Time Complexity
The time complexity is O(n), where `n` is the length of the original `nums` array. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) due to the stack and the `ans` list.

### Algorithm
1. Extend the array by concatenating `nums` with itself.
2. Initialize `ans` with -1 and an empty stack.
3. Loop through the extended array:
   - Update the next greater element for indices on the stack where the current element is greater.
   - Push the current index onto the stack.
4. Return the first half of `ans`.
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        ans = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return ans[:len(nums)//2]
