# Time Complexity: O(n), where n is the length of the array `nums`.
# We iterate through the array once, updating `reach` and `curEnd`, which makes the time complexity linear.

# Space Complexity: O(1), as we only use a few extra variables (`jumps`, `reach`, and `curEnd`) that take constant space regardless of the input size.

# INTUITION:
# The goal is to find the minimum number of jumps needed to reach the last index. At every step, we maximize how far we can go with the current number of jumps.
# We try to make a jump when we reach the furthest point of the current jump (`curEnd`). This ensures we minimize the total number of jumps.

# ALGO:
# 1. **Initialize variables**:
#    - `jumps` to count the number of jumps.
#    - `reach` to keep track of the farthest position we can reach.
#    - `curEnd` to denote the furthest point we can jump to with the current number of jumps.
# 2. **Iterate through the array**:
#    - For each element, update `reach` to be the maximum of the current `reach` and the current index plus the value at that index (i.e., `i + nums[i]`).
#    - If the current index reaches `curEnd`, it means we have to make a jump, so increment the jump counter and update `curEnd` to `reach`.
# 3. **Return the result**:
#    - At the end of the loop, the number of jumps will be the minimum needed to reach the last index.

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Step 1: Initialize the variables
        jumps = 0
        reach, curEnd = 0, 0

        # Step 2: Iterate through the array
        for i in range(len(nums) - 1):  # We don't need to check the last element
            # Update the maximum reach
            reach = max(reach, i + nums[i])

            # If we reach the current end, make a jump
            if i == curEnd:
                jumps += 1
                curEnd = reach

        # Step 3: Return the total jumps needed
        return jumps
