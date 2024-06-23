"""
### Problem
Given two arrays `nums1` and `nums2` where `nums1` is a subset of `nums2`, find the next greater element for each element in `nums1` in the array `nums2`. The Next Greater Element of a number `x` in `nums1` is the first greater number to its right in `nums2`. If it does not exist, return -1 for this number.

### Intuition
To solve the problem of finding the next greater element for each element in `nums1`, we can use a stack to keep track of elements for which we haven't found the next greater element yet. As we iterate through `nums2`, we will update the next greater elements and store the results in a hashmap for quick lookup when constructing the final result for `nums1`.

### Approach
1. **Initialize Data Structures**: Create a list `tempAns` of the same length as `nums2`, initialized to -1, to store the next greater elements. Initialize an empty stack to keep track of indices and an empty hashmap to map elements in `nums2` to their indices.
2. **Iterate Through nums2**: Loop through each element in `nums2`:
   - While the stack is not empty and the current element is greater than the element at the index on the top of the stack:
     - Pop the index from the stack.
     - Update the next greater element for the popped index in `tempAns`.
   - Push the current index onto the stack.
   - Map the current element to its index in the hashmap.
3. **Construct the Result**: For each element in `nums1`, look up its next greater element in `tempAns` using the index found in the hashmap and append the result to the answer list.
4. **Return the Result**: Return the constructed answer list.

### Time Complexity
The time complexity is O(n + m), where `n` is the length of `nums2` and `m` is the length of `nums1`. Each index is pushed and popped from the stack at most once, and hashmap lookups are O(1).

### Space Complexity
The space complexity is O(n) due to the stack, the hashmap, and the `tempAns` list.

### Algorithm
1. Initialize `tempAns` with -1 and an empty stack.
2. Initialize an empty hashmap.
3. Loop through `nums2`:
   - Update the next greater element for indices on the stack where the current element is greater.
   - Push the current index onto the stack.
   - Map the current element to its index in the hashmap.
4. Construct the result for `nums1` using the `tempAns` and the hashmap.
5. Return the result.
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempAns = [-1] * len(nums2)
        stack = []
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
            while stack and nums2[stack[-1]] < nums2[i]:
                tempAns[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)

        ans = []
        for num in nums1:
            ans.append(tempAns[hashmap[num]])

        return ans
