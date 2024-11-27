# Time Complexity: O(n), where n is the number of stairs.
# - We iterate from 3 to n to calculate the number of ways to climb the stairs.

# Space Complexity: O(1).
# - We use only two variables (`a` and `b`) to store intermediate results, avoiding the need for additional memory.

# INTUITION:
# - This problem is a classic example of the Fibonacci sequence.
# - To climb to the nth step, you can either come from the (n-1)th step (1 step away) or the (n-2)th step (2 steps away).
# - Therefore, the number of ways to climb to the nth step is the sum of the number of ways to climb to the (n-1)th and (n-2)th steps.
# - The base cases are:
#   - For n = 1, there is 1 way.
#   - For n = 2, there are 2 ways.

# ALGORITHM:
# 1. Handle the base cases explicitly:
#    - If n = 1, return 1.
#    - If n = 2, return 2.
# 2. Initialize two variables `a` and `b` to represent the number of ways to climb to the first and second steps, respectively.
# 3. Use a loop from step 3 to step n, updating `a` and `b` to reflect the number of ways to climb to the current step.
# 4. At the end, return `b`, which represents the number of ways to climb to the nth step.

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize for the first two steps
        a, b = 1, 2

        # Compute ways for steps 3 to n
        for i in range(3, n + 1):
            a, b = b, a + b  # Update `a` to `b` and `b` to `a + b`

        return b

# Example Usage:
# Input: n = 3
# Output: 3
# Explanation: There are 3 ways to climb 3 stairs: [1,1,1], [1,2], [2,1].

# Input: n = 5
# Output: 8
# Explanation: There are 8 ways to climb 5 stairs.
