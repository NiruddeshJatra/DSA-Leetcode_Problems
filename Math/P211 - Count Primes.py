# Time Complexity: O(n * log(log(n)))
# - The Sieve of Eratosthenes algorithm efficiently marks non-prime numbers. 
# - The inner loop runs approximately n/2 + n/3 + n/5 + ... ≈ n * log(log(n)) iterations.

# Space Complexity: O(n)
# - A boolean array `isPrime` of size `n` is used to track whether each number is prime.

# INTUITION:
# The problem requires counting all prime numbers less than `n`. A prime number is divisible only by 1 and itself.
# Using the Sieve of Eratosthenes is an efficient way to solve this problem:
# - It eliminates multiples of each prime starting from 2, leaving only prime numbers marked as True in the array.

# ALGO:
# 1. Handle edge cases: If `n` is less than or equal to 1, return 0 (no primes exist).
# 2. Create a boolean array `isPrime` of size `n` initialized to True:
#    - Set `isPrime[0]` and `isPrime[1]` to False since 0 and 1 are not primes.
# 3. Iterate over numbers starting from 2 up to the square root of `n`:
#    - For each number that is still marked as prime, mark all its multiples as non-prime.
#    - Start marking from `num * num` because smaller multiples will have already been marked by smaller primes.
# 4. Return the count of True values in `isPrime`, which represents the total number of primes less than `n`.

class Solution:
    def countPrimes(self, n: int) -> int:
        # Handle edge case
        if n <= 1:
            return 0

        # Create a boolean array to track prime numbers
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False  # 0 and 1 are not prime numbers

        # Use Sieve of Eratosthenes to eliminate non-prime numbers
        for num in range(2, int(n**0.5) + 1):
            if isPrime[num]:
                # Mark multiples of the current prime as non-prime
                for i in range(num * num, n, num):
                    isPrime[i] = False

        # Count and return the number of primes
        return sum(isPrime)
