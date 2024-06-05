# Time Complexity: O(log n)
# Space Complexity: O(log n) due to the recursion stack

# INTUITION:
# The goal is to efficiently compute `x` raised to the power `n`, which can be large and potentially negative.
# Using the concept of exponentiation by squaring, we can reduce the number of multiplications needed.
# This approach divides the problem into smaller subproblems, leveraging the properties of exponents:
# - If `n` is even, we can reduce the problem to (x^2)^(n/2).
# - If `n` is odd, we handle the extra factor by multiplying x with the result of (x^2)^((n-1)/2).
# By recursively applying these reductions, we achieve an efficient solution.

# ALGO:
# 1. Define a helper function `helper(x, n)` that computes `x` raised to the power `n` recursively.
#    a. Base cases: 
#       - If `n` is 0, return 1 (anything raised to the power 0 is 1).
#       - If `n` is 1, return `x` (base case for recursion).
#       - If `x` is 0, return 0 (0 raised to any power is 0).
#    b. If `n` is even, return `helper(x*x, n//2)`.
#    c. If `n` is odd, return `x * helper(x*x, n//2)`.
# 2. Call `helper` with the absolute value of `n` to handle negative exponents.
# 3. If `n` is non-negative, return the result from `helper`.
# 4. If `n` is negative, return the reciprocal of the result from `helper`.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if x == 0:
                return 0
            if n % 2 == 0:
                return helper(x * x, n // 2)
            else:
                return x * helper(x * x, n // 2)

        ans = helper(x, abs(n))
        if n >= 0:
            return ans
        return 1 / ans
