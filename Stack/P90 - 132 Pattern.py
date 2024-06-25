"""
### Problem
Given an array of n integers `nums`, a 132 pattern is a subsequence of three integers `nums[i]`, `nums[j]`, `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`. Your task is to find out whether there is a 132 pattern in the array.

### Intuition
The idea is to use a stack to maintain possible candidates for the `2` in the `132` pattern while traversing the array from right to left. By doing this, we can efficiently keep track of the `3` in the `132` pattern and check if a valid `1` is found.

### Approach
1. Initialize `num3` to a very small number, which will represent the potential `3` in the `132` pattern.
2. Use a stack to keep track of the potential candidates for the `2` in the `132` pattern.
3. Traverse the array from right to left:
   - For each element, if it's less than `num3`, a valid `132` pattern is found.
   - While the stack is not empty and the current element is greater than the top element of the stack, pop from the stack and update `num3` to this popped value.
   - Push the current element onto the stack.
4. If no valid `132` pattern is found by the end of the traversal, return `False`.

### Algorithm
1. Initialize `num3` to a very small number.
2. Create an empty stack.
3. Loop through the elements of the array from right to left:
   - If the current element is less than `num3`, return `True`.
   - While the stack is not empty and the top of the stack is less than the current element, pop from the stack and set `num3` to this value.
   - Push the current element onto the stack.
4. Return `False` if no `132` pattern is found.

### Time Complexity
The time complexity is O(n), where n is the number of elements in the array, as each element is processed at most twice.

### Space Complexity
The space complexity is O(n) for the stack.

### Code
"""

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num3 = -(10**10)  # Initialize num3 to a very small number
        stack = []  # Stack to keep track of potential candidates for the '2' in the '132' pattern
        
        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            # If current element is less than num3, a 132 pattern is found
            if nums[i] < num3:
                return True
            # Update num3 while the stack has elements less than the current element
            while stack and stack[-1] < nums[i]:
                num3 = stack.pop()
            # Push the current element onto the stack
            stack.append(nums[i])
        
        # No 132 pattern found
        return False
