# Time Complexity:
# - O(log n), where n is the maximum of a and b.
# - In the worst case, we need to handle each bit position, and there are at most 32 bit positions for integers.

# Space Complexity:
# - O(1), as we only use a constant amount of space regardless of input size.

# INTUITION:
# This solution implements binary addition without using the + operator by simulating how addition works at the bit level.
# Binary addition involves two operations:
# 1. XOR (^): Adds bits without considering carry
# 2. AND with left shift (& <<1): Generates the carry
#
# For example, to add 5 (101) and 3 (011):
# - XOR gives 6 (110) - where bits are different
# - Carry gives 2 (010) - where both bits are 1, shifted left
# - We then repeat with 6 and 2 until no carry remains
#
# The mask is used to handle negative numbers in Python's representation by limiting to 32 bits.

# ALGO:
# 1. Use a 32-bit mask (0xffffffff) to limit calculations to 32 bits.
# 2. While b (the carry) is non-zero:
#    a. Calculate new carry using AND operation and left shift.
#    b. Calculate sum without carry using XOR operation.
#    c. Set b to the new carry for next iteration.
# 3. Handle potential negative number when returning result.

class Solution:
   def getSum(self, a: int, b: int) -> int:
       # 32-bit mask to limit integers to 32 bits
       MASK = 0xffffffff
       
       # Perform addition until no carry remains
       while (b & MASK) > 0:
           # Calculate the carry bits (where both bits are 1)
           carry = (a & b) << 1
           
           # Calculate the sum without considering carry (XOR)
           a = (a ^ b) & MASK
           
           # Set b to the carry for the next iteration
           b = carry
       
       # Handle negative numbers in Python
       # If the result is negative (has 1 in MSB position)
       if (a >> 31) & 1:
           # Two's complement to get the negative value
           return ~(a ^ MASK)
       
       # Return the positive result
       return a
