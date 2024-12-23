# Time Complexity: O(log(n)^2), where n is the absolute value of `dividend`.
# - In the outer loop, the dividend is reduced by at least half in each iteration due to the shifting process.
# - In the inner loop, the bit-shifting operations take O(log(n)) time.
# - Total time complexity is approximately O(log(n)^2).

# Space Complexity: O(1).
# - No additional space is used apart from a few variables.

# INTUITION:
# The goal is to divide two integers without using multiplication, division, or modulo operators.
# This is achieved using bit manipulation. Division is implemented by repeatedly subtracting the divisor
# from the dividend in powers of 2 (using bit shifts).

# ALGO:
# 1. Handle special cases:
#    - Division by zero: return INT_MAX.
#    - Overflow case (-2^31 divided by -1): return INT_MAX.
# 2. Determine the sign of the result based on the dividend and divisor.
# 3. Work with absolute values of the dividend and divisor.
# 4. Use bit-shifting to speed up the subtraction process:
#    - Find the largest power of 2 such that (divisor * 2^k) ≤ dividend.
#    - Subtract (divisor * 2^k) from the dividend and add 2^k to the result.
# 5. Apply the sign to the result.
# 6. Ensure the result is within the 32-bit signed integer range.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1
        
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Initialize result and sign
        ans = 0
        sign = +1 if dividend ^ divisor >= 0 else -1  # Determine if the result is positive or negative

        # Work with absolute values
        n, d = abs(dividend), abs(divisor)
        while n >= d:
            count = 0
            # Find the largest power of 2 such that d * 2^(count+1) ≤ n
            while n >= (d << (count + 1)):
                count += 1

            # Add 2^count to the result and subtract d * 2^count from n
            ans += 1 << count
            n -= d << count

        # Apply the sign
        ans *= sign

        # Clamp the result within the 32-bit signed integer range
        if not (-2**31 <= ans <= 2**31 - 1):
            return 2**31 - 1

        return ans
