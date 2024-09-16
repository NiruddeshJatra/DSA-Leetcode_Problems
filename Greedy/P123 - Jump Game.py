# Time Complexity: O(n), where n is the length of the array `nums`. 
# We iterate through the array once in reverse, making the time complexity linear.

# Space Complexity: O(1), as we only use a few extra variables (`isPossible` and `jumpNeeded`) 
# that take constant space regardless of the input size.

# INTUITION:
# The goal is to determine if it's possible to reach the end of the array, where each element represents the maximum jump length at that position. 
# We check from the end of the array backwards to see if we can "escape" any position with a value of 0, which would trap us.

# ALGO:
# 1. **Handle Base Case**:
#    - If the array has only one element, we can trivially reach the end, so return `True`.
# 2. **Iterate from Right to Left**:
#    - Loop through the array from the second-to-last element to the first.
#    - Keep track of whether it's possible to reach the end from a certain point (`isPossible`).
#    - If you encounter a `0`, update the `isPossible` flag to `False` and initialize the jump needed (`jumpNeeded`) to escape the zero.
# 3. **Handle Non-Zero Elements**:
#    - If we encounter an element larger than the `jumpNeeded`, reset `isPossible` to `True`, as we can escape the zero and continue the path forward.
# 4. **Return the Result**:
#    - At the end of the loop, return whether it's possible to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Step 1: Handle the base case where there's only one element
        if len(nums) == 1:
            return True

        # Step 2: Initialize the variables
        isPossible = True

        # Step 3: Iterate from right to left
        for i in range(len(nums)-2, -1, -1):  # Start from second-last element and move to the first
            if isPossible and nums[i] == 0:
                # Step 4: If we hit a zero, mark it as not possible and set jumpNeeded to 1
                isPossible = False
                jumpNeeded = 1
            elif not isPossible:
                # Step 5: If we're not in a possible state, check if current element can jump out
                if nums[i] > jumpNeeded:
                    isPossible = True  # Reset the state to possible if we can escape the zero
                else:
                    jumpNeeded += 1  # Increment the jumps needed to escape the zero

        # Step 6: Return whether it's possible to reach the end
        return isPossible
