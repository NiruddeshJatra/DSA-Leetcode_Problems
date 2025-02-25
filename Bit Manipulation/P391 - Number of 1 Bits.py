# Time Complexity:
# - O(k), where k is the number of set bits (1s) in the binary representation of n.
# - The while loop iterates exactly once for each set bit in n.

# Space Complexity:
# - O(1), as we only use a constant amount of extra space regardless of the input size.

# INTUITION:
# This solution uses Brian Kernighan's algorithm, which is a clever bit manipulation technique.
# When we perform n & (n-1), it always flips the rightmost set bit (1) in n to 0.
# 
# For example, if n = 10110:
# - n-1 = 10101 (the rightmost 1 becomes 0, and all bits to the right become 1)
# - n & (n-1) = 10110 & 10101 = 10100 (the rightmost 1 is cleared)
# 
# By counting how many times we can perform this operation until n becomes 0,
# we directly count the number of set bits without having to check each bit position.

# ALGO:
# 1. Initialize a counter for the number of set bits.
# 2. Repeatedly clear the rightmost set bit using the operation n = n & (n-1).
# 3. Increment the counter each time we clear a bit.
# 4. Continue until n becomes 0 (no more set bits).
# 5. Return the counter.

class Solution:
   def hammingWeight(self, n: int) -> int:
       setBitCount = 0
       
       # Continue until all bits are cleared
       while n:
           # Clear the rightmost set bit
           n &= (n - 1)
           # Increment our counter
           setBitCount += 1
       
       return setBitCount
