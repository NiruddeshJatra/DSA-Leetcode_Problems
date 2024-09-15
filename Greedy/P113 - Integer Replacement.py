# Time Complexity: O(log n), where n is the input integer. Each time the number is halved (when even) or adjusted by 1 (when odd), reducing the problem size by about half. Therefore, the number of steps is proportional to the logarithm of the input.
# Space Complexity: O(1), as we are only using a few variables (cnt and n) to store the number of operations and the current value of n, without any additional data structures.

# INTUITION:
# The goal is to reduce the given integer `n` to 1 by performing the minimum number of operations. 
# In each operation, if `n` is even, it can be halved. If `n` is odd, we have two options: either increment or decrement it, aiming to make the number even so it can be halved in future steps.
# 
# **Key Insight**:
# - If `n` is even, we divide by 2.
# - If `n` is odd, we need to decide whether to increment or decrement it. The decision is based on minimizing the number of future steps: if incrementing leads to a number that can be halved multiple times, it may be more optimal. However, if `n == 3`, decrementing is the best choice because it leads directly to 2 and then 1.
#
# **Greedy Approach**:
# - For odd numbers, the strategy involves analyzing the results of incrementing vs. decrementing. If adding 1 to `n` makes the next number divisible by 4, it's more optimal to increment; otherwise, decrement. This is because dividing by 4 reduces the size of `n` faster than dividing by 2.

# ALGO:
# 1. **Initialize Count**: 
#    - Initialize a counter `cnt` to track the number of operations.
# 2. **While Loop to Reduce n**:
#    - While `n` is not equal to 1, check whether `n` is even or odd.
#    - If `n` is even, divide it by 2.
#    - If `n` is odd, decide between incrementing or decrementing:
#      - If incrementing leads to a number divisible by 4 (except when `n == 3`), increment.
#      - Otherwise, decrement.
# 3. **Return Count**:
#    - After reducing `n` to 1, return the total number of operations.

class Solution:
    def integerReplacement(self, n: int) -> int:
        # Step 1: Initialize the operation counter
        cnt = 0

        # Step 2: Process the number until it becomes 1
        while n != 1:
            if n % 2 == 0:
                # Step 2.1: If n is even, divide by 2
                n //= 2
            else:
                # Step 2.2: If n is odd, decide whether to increment or decrement
                if n != 3 and ((n + 1) // 2) % 2 == 0:
                    n += 1
                else:
                    n -= 1

            # Step 3: Increment the operation counter
            cnt += 1

        # Step 4: Return the total number of operations
        return cnt
