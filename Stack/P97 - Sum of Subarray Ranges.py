"""
### Problem
Given an array of integers `nums`, find the sum of the ranges of all subarrays. A range of a subarray is defined as the difference between the maximum and minimum elements in that subarray.

### Intuition
To efficiently calculate the sum of the ranges of all subarrays, we can use a monotonic stack. The idea is to use two passes with the stack: 
1. One pass to calculate the contribution of each element when it acts as the maximum element in a subarray.
2. Another pass to calculate the contribution of each element when it acts as the minimum element in a subarray.

### Approach
1. **Initialization**:
   - Define `inf` as infinity to handle edge cases.
   - Initialize `ans` to store the final result.
   - Create an array `arr` with `inf` at both ends to handle boundaries for maximum element calculation.
   - Initialize an empty stack.
2. **First Pass**:
   - Iterate through the array:
     - While the stack is not empty and the current element is greater than the element corresponding to the top index of the stack:
       - Pop the top index from the stack.
       - Calculate the number of subarrays where the popped element is the maximum.
       - Update `ans` with the contribution of the popped element as the maximum.
     - Push the current index onto the stack.
3. **Second Pass**:
   - Create an array `arr` with `-inf` at both ends to handle boundaries for minimum element calculation.
   - Reinitialize the stack.
   - Iterate through the array:
     - While the stack is not empty and the current element is less than the element corresponding to the top index of the stack:
       - Pop the top index from the stack.
       - Calculate the number of subarrays where the popped element is the minimum.
       - Update `ans` with the contribution of the popped element as the minimum.
     - Push the current index onto the stack.
4. **Return Result**: The final value of `ans`.

### Time Complexity
The time complexity is O(n) where n is the number of elements in the array. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack and the modified array.

### Code
"""

from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        inf = float('inf')
        ans = 0
        arr = [inf] + nums + [inf]
        stack = []

        # First pass to calculate maximum contributions
        for i2 in range(len(arr)):
            while stack and arr[i2] > arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                left = index - i1
                right = i2 - index
                ans += arr[index] * right * left
            stack.append(i2)

        arr = [-inf] + nums + [-inf]
        stack = []

        # Second pass to calculate minimum contributions
        for i2 in range(len(arr)):
            while stack and arr[i2] < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                left = index - i1
                right = i2 - index
                ans -= arr[index] * right * left
            stack.append(i2)

        return ans
