# Time Complexity: O(log(x)), where x is the input value.
# - Binary search divides the search range in half at every step.

# Space Complexity: O(1).
# - No extra space is used apart from a few variables.

# INTUITION:
# - The problem is equivalent to finding the largest integer `n` such that `n^2 <= x`.
# - Binary search is an effective method since the values of `n^2` increase monotonically as `n` increases.
# - By narrowing down the search range, we efficiently pinpoint the integer square root.

# ALGORITHM:
# 1. Handle base cases: if `x` is 0 or 1, return `x` immediately.
# 2. Use binary search within the range `[0, x]`:
#    - Calculate the midpoint.
#    - Check if `mid * mid` is less than or equal to `x`:
#      - If yes, move `left` to `mid + 1` (to search for larger values).
#      - Otherwise, move `right` to `mid` (to search for smaller values).
# 3. When the loop terminates, `left - 1` is the largest integer whose square is less than or equal to `x`.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:  # Handle cases for x = 0 and x = 1
            return x

        # Binary search range
        left, right = 0, x

        while left < right:
            mid = (left + right) // 2
            # If mid * mid is less than or equal to x, move the left pointer
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid  # Otherwise, adjust the right pointer

        return left - 1  # Return the largest valid integer

# Example Usage:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is approximately 2.828, and the integer part is 2.

# Input: x = 0
# Output: 0
# Explanation: The square root of 0 is 0.

# Input: x = 1
# Output: 1
# Explanation: The square root of 1 is 1.
