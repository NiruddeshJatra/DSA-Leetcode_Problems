# Time Complexity:
# - O(1), as we always process exactly 32 bits regardless of the input size.
# - The loop executes a constant number of iterations (32).

# Space Complexity:
# - O(1), as we only use a constant amount of extra space.

# INTUITION:
# To reverse the bits of a 32-bit integer, we need to take each bit from its original position
# and move it to the opposite position. The most significant bit (MSB) becomes the least significant bit (LSB)
# and vice versa.
#
# We can process the number bit by bit from right to left (LSB to MSB). For each bit in the original number:
# 1. Extract the rightmost bit (LSB) of the original number
# 2. Shift the result left by 1 to make room for the new bit
# 3. Add the extracted bit to the result using OR operation
# 4. Shift the original number right by 1 to process the next bit
#
# This approach is like reading the original number from right to left and writing it from left to right.

# ALGO:
# 1. Initialize a result variable to 0.
# 2. Iterate exactly 32 times (for each bit position in a 32-bit integer):
#    a. Left shift the result by 1 to make room for the next bit.
#    b. Extract the rightmost bit of n using bitwise AND with 1.
#    c. Add this bit to the result using bitwise OR.
#    d. Right shift n by 1 to process the next bit.
# 3. Return the final result.

class Solution:
   def reverseBits(self, n: int) -> int:
       # Initialize result to 0
       result = 0
       
       # Process all 32 bits of the input
       for i in range(32):
           # Shift result left to make room for the next bit
           result <<= 1
           
           # Extract the rightmost bit of n and add it to result
           result |= (n & 1)
           
           # Shift n right to process the next bit
           n >>= 1
       
       return result
