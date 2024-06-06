# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion depth

# INTUITION:
# The problem involves calculating large powers efficiently, which can be handled using 
# the technique known as exponentiation by squaring. This method reduces the number of 
# multiplications needed, making it very efficient for large exponents. We break down 
# the problem into smaller subproblems, leveraging the properties of exponents to 
# combine results.

# ALGO:
# 1. DEFINE a recursive function getPow(x, n) to calculate x raised to the power n 
#    modulo MOD using exponentiation by squaring.
#    - BASE CASE: If n is 0, return 1.
#    - BASE CASE: If n is 1, return x modulo MOD.
#    - If n is even, calculate the power for half the exponent and square it.
#    - If n is odd, calculate the power for half the exponent, square it, and multiply 
#      by x once more.
# 2. CALCULATE the power of 4 and 5 for the appropriate number of positions.
# 3. MULTIPLY the results together, taking care to use modulo at each step to prevent 
#    overflow.
# 4. RETURN the final result modulo 10^9 + 7.

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def getPow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x % MOD
            if x == 0:
                return 0
            power = getPow((x * x) % MOD, n // 2)
            if n % 2 != 0:
                power = (x * power) % MOD
            return power

        p, q = getPow(4, n // 2) % MOD, getPow(5, n // 2) % MOD
        if n % 2 == 0:
            ans = p * q
        else:
            ans = 5 * p * q
        return ans % MOD
