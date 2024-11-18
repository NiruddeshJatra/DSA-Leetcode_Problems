# INTUITION:
# The problem requires minimizing the difference between the maximum and minimum values of the array 
# after at most 3 elements are removed. Sorting is a natural choice because it arranges the elements 
# in increasing order, making it straightforward to focus on specific ranges of the array.
#
# Key observations:
# 1. Removing up to 3 elements can impact either the smallest or largest values of the array.
# 2. After sorting, the smallest difference can be achieved by considering the following scenarios:
#    - Removing the 3 smallest elements (focus on the top elements).
#    - Removing the 2 smallest and 1 largest element.
#    - Removing the 1 smallest and 2 largest elements.
#    - Removing the 3 largest elements (focus on the bottom elements).
# 3. Each scenario corresponds to comparing a small portion of the sorted array to minimize the difference.
#
# By iterating through these scenarios, the minimum difference can be determined efficiently.

# ALGORITHM:
# 1. Sort the array to easily access the smallest and largest elements.
# 2. If the array has fewer than 5 elements, the result is 0 (since we can remove all but one).
# 3. Calculate the differences for the 4 possible scenarios:
#    - `nums[-4] - nums[0]`: Keep the largest 4 elements.
#    - `nums[-3] - nums[1]`: Remove the smallest 1 and largest 1 elements.
#    - `nums[-2] - nums[2]`: Remove the smallest 2 and largest 2 elements.
#    - `nums[-1] - nums[3]`: Keep the smallest 4 elements.
# 4. Return the minimum difference among these scenarios.

# TIME COMPLEXITY:
# O(n * log(n)), where `n` is the length of `nums`:
# - Sorting the array dominates the time complexity.

# SPACE COMPLEXITY:
# O(1):
# - No additional space is used apart from a few variables.

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # If the array has fewer than 5 elements, we can remove all but one
        if len(nums) < 5:
            return 0
        
        # Calculate the differences for the 4 scenarios
        return min(
            nums[-4] - nums[0],  # Keep the largest 4 elements
            nums[-3] - nums[1],  # Remove the smallest 1 and largest 1
            nums[-2] - nums[2],  # Remove the smallest 2 and largest 2
            nums[-1] - nums[3]   # Keep the smallest 4 elements
        )
