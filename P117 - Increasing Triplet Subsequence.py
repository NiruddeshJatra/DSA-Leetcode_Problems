# Time Complexity: O(n), where n is the length of the array `nums`. We iterate through the array once, making the time complexity linear.
# Space Complexity: O(1), since we are only using a constant amount of extra space for the variables `first` and `second`.

# INTUITION:
# The problem is to determine if there exists an increasing subsequence of length 3 in the given array. This means we need to find three numbers such that `nums[i] < nums[j] < nums[k]` with `i < j < k`.
#
# **Key Insight**:
# - We can maintain two variables, `first` and `second`, to represent the smallest and second smallest values found so far in the array.
# - As we iterate through the array, we attempt to update these two variables. If we encounter a value greater than both `first` and `second`, it means we've found an increasing triplet.

# ALGO:
# 1. **Initialize Two Variables**:
#    - Set `first` and `second` to infinity (`float('inf')`). These will store the smallest and second smallest values we encounter during the iteration.
# 2. **Traverse the Array**:
#    - For each number in `nums`, compare it with `first` and `second`:
#        - If the current number is smaller than or equal to `first`, update `first` to this number.
#        - Otherwise, if it is smaller than or equal to `second` (but greater than `first`), update `second`.
#        - If it is greater than both `first` and `second`, return `True`, as we have found the triplet.
# 3. **Return False if No Triplet Found**:
#    - If the loop completes without finding a valid triplet, return `False`.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Step 1: Initialize the smallest and second smallest values to infinity
        first = second = float('inf')

        # Step 2: Traverse the array
        for i in nums:
            if i <= first:
                # Update `first` if the current number is smaller than or equal to it
                first = i
            elif i <= second:
                # Update `second` if the current number is smaller than or equal to it but greater than `first`
                second = i
            else:
                # If the current number is greater than both `first` and `second`, return True
                return True

        # Step 3: If no increasing triplet is found, return False
        return False
