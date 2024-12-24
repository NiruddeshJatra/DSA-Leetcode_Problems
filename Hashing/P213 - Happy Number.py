# Time Complexity: O(log(n)), where n is the input number.
# - Each time we sum the squares of digits of n, the result will be smaller than n.
# - Hence, the number of iterations will be proportional to the number of digits in n, which is O(log(n)).
# - Each iteration involves summing the squares of digits, which takes O(log(n)) time.

# Space Complexity: O(log(n)), where n is the input number.
# - The set `squared` stores previously seen sums, which is at most proportional to the number of unique sums that can be formed from the digits of n.
# - In the worst case, this requires space proportional to the number of digits in n, O(log(n)).

# INTUITION:
# The goal is to determine if a number is "happy." A number is happy if, by repeatedly summing the squares of its digits, 
# the result eventually equals 1. If the sum enters a cycle that does not contain 1, the number is not happy.
# The key observation is that numbers that aren't happy will eventually repeat, forming a cycle.
# Hence, we track the sums of squares of digits using a set to detect any cycles.

# ALGO:
# 1. Initialize a set `squared` to store the numbers we encounter while summing the squares of digits.
# 2. Start with the given number `n`.
# 3. In each iteration, sum the squares of the digits of `n`.
# 4. If the result is 1, return True (the number is happy).
# 5. If the result has been encountered before (i.e., it's in the set `squared`), return False (the number is stuck in a cycle).
# 6. Otherwise, continue with the new sum.
# 7. Repeat until we either reach 1 or detect a cycle.

class Solution:
    def isHappy(self, n: int) -> bool:
        squared = set()  # Set to track sums that have been encountered
        squared.add(n)   # Add the initial number to the set
        
        while True:
            # Sum the squares of the digits of n
            total = sum(int(digit) ** 2 for digit in str(n))
            
            # If the total is 1, the number is happy
            if total == 1:
                return True
            
            # If we've seen this total before, it's in a cycle
            if total in squared:
                return False
            
            # Update n for the next iteration and add the total to the set
            n = total
            squared.add(total)
