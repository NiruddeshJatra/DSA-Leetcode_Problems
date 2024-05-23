import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            total = 0
            for i in nums:
                total += math.ceil(i / mid)
            if total > threshold:
                l = mid + 1
            else:
                r = mid

        return l

# Time Complexity: O(n log m), where n is the number of elements in nums and m is the maximum element in nums.
# Space Complexity: O(1), since we are using a constant amount of additional space.

# INTUITION:
# The problem requires us to find the smallest integer divisor such that the sum of the results of dividing each element in nums by this divisor, rounded up to the nearest integer, is less than or equal to a given threshold.
# Using binary search on the range of possible divisors (from 1 to the maximum element in nums) allows us to efficiently narrow down the smallest valid divisor.
# The key insight is that if a certain divisor results in a sum that is within the threshold, then any larger divisor will also be within the threshold.

# ALGO:
# 1. INITIALIZE l (left) to 1 (smallest possible divisor) and r (right) to max(nums) (largest possible divisor).
# 2. While l is less than r:
#    2.1. Calculate mid, the midpoint of l and r.
#    2.2. Initialize total to 0. This variable will store the sum of the rounded-up division results.
#    2.3. For each element i in nums:
#        - Calculate the division result of i by mid, rounded up to the nearest integer using math.ceil, and add it to total.
#    2.4. If total exceeds the threshold, set l to mid + 1, meaning mid is too small a divisor.
#    2.5. Otherwise, set r to mid, meaning mid is a valid divisor, but we try for a smaller one.
# 3. RETURN l, which will be the smallest divisor that results in a sum within the threshold.

# EXPLANATION OF APPROACH:
# - We start by setting the binary search bounds between 1 and the maximum element in nums.
# - We iteratively calculate the midpoint and check if it can be a valid divisor by computing the sum of the rounded-up division results.
# - If the sum exceeds the threshold, we need a larger divisor, so we adjust the left bound.
# - If the sum is within the threshold, we adjust the right bound to try finding a smaller valid divisor.
# - This process continues until the left and right bounds converge, giving us the smallest divisor that satisfies the condition.
