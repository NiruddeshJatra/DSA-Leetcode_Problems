"""
### Problem
Given an array of integers `arr`, find the sum of the minimum value of all subarrays of `arr`. The result should be returned modulo \(10^9 + 7\).

### Intuition
To efficiently calculate the sum of the minimum values of all subarrays, we can use a monotonic stack. The idea is to keep track of the indices of the array elements in increasing order in the stack. When we find an element that is smaller than the element corresponding to the top index of the stack, we can calculate the number of subarrays where the element at the top of the stack is the minimum.

### Approach
1. **Initialization**:
   - Append `0` to the array to handle the end of the array and ensure all elements are processed.
   - Initialize `ans` to accumulate the sum of the minimum values of all subarrays.
   - Initialize `stack` with `-1` to handle the left boundary.
2. **Iterate Through the Array**:
   - For each element in the array, while the stack is not empty and the current element is smaller than the element corresponding to the top index of the stack:
     - Pop the top index from the stack.
     - Calculate the number of subarrays where the popped element is the minimum.
     - Add the contribution of the popped element to `ans`.
   - Push the current index onto the stack.
3. **Return Result**: The accumulated `ans` modulo \(10^9 + 7\).

### Time Complexity
The time complexity is O(n) where n is the number of elements in the array. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack.

### Code
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)  # Append 0 to handle the end of the array
        ans = 0
        stack = [-1]  # Initialize stack with -1 to handle the left boundary
        
        for i2 in range(len(arr)):
            while stack and arr[i2] < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                left = index - i1  # Distance to the previous smaller element
                right = i2 - index  # Distance to the next smaller element
                ans += arr[index] * left * right  # Contribution to the result
            stack.append(i2)
        
        return ans % (10**9 + 7)
