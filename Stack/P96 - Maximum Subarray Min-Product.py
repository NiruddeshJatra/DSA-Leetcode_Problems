"""
### Problem
Given an array of integers `arr`, find the maximum sum of the minimum value of any subarray multiplied by the sum of that subarray. The result should be returned modulo \(10^9 + 7\).

### Intuition
To efficiently calculate the maximum sum of the minimum value of any subarray multiplied by the sum of that subarray, we can use a monotonic stack. The idea is to keep track of the indices of the array elements in increasing order in the stack. When we find an element that is smaller than the element corresponding to the top index of the stack, we can calculate the maximum product for the subarray where the element at the top of the stack is the minimum.

### Approach
1. **Initialization**:
   - Append `0` to the array to handle the end of the array and ensure all elements are processed.
   - Initialize `ans` to store the maximum product.
   - Initialize `stack` with `-1` to handle the left boundary.
   - Initialize `sums` with `0` to store prefix sums.
2. **Iterate Through the Array**:
   - For each element in the array, update the `sums` array with the prefix sum.
   - While the stack is not empty and the current element is smaller than the element corresponding to the top index of the stack:
     - Pop the top index from the stack.
     - Calculate the subarray sum using the prefix sums.
     - Update `ans` with the maximum product.
   - Push the current index onto the stack.
3. **Return Result**: The maximum product `ans` modulo \(10^9 + 7\).

### Time Complexity
The time complexity is O(n) where n is the number of elements in the array. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack and the prefix sums array.

### Code
"""

from typing import List

class Solution:
    def maxSumMinProduct(self, arr: List[int]) -> int:
        arr.append(0)  # Append 0 to handle the end of the array
        ans = 0
        stack = [-1]  # Initialize stack with -1 to handle the left boundary
        sums = [0]  # Initialize sums with 0 to store prefix sums

        for i2 in range(len(arr)):
            sums.append(arr[i2] + sums[-1])  # Update prefix sums

            while stack and arr[i2] < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                subarray_sum = sums[i2] - sums[i1 + 1]  # Calculate subarray sum
                ans = max(ans, arr[index] * subarray_sum)  # Update maximum product
            stack.append(i2)

        return ans % (10**9 + 7)
