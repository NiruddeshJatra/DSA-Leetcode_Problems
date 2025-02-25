# Time Complexity:
# - O(n), where n is the input integer.
# - We iterate through numbers from 1 to n once, performing constant-time operations for each.

# Space Complexity:
# - O(n) for the result array which contains n+1 elements.

# INTUITION:
# The problem asks us to count the number of 1 bits (set bits) in the binary representation of each number from 0 to n.
# Instead of calculating each number independently (which would be O(n log n)), we can use dynamic programming to leverage 
# previously calculated results.
#
# There are two key insights:
# 1. For even numbers (i): The number of set bits is the same as i/2 (right shift by 1)
#    - Example: bits(4) = bits(2) because 4 (100) is just 2 (10) with a 0 appended
# 2. For odd numbers (i): The number of set bits is one more than the number of set bits in i-1
#    - Example: bits(5) = bits(4) + 1 because 5 (101) is just 4 (100) with the last bit flipped to 1
#
# This approach allows us to build our answer iteratively using previously computed values.

# ALGO:
# 1. Initialize the result array with 0 (the number of set bits in 0).
# 2. Iterate through numbers from 1 to n.
# 3. For each number i:
#    a. If i is even (LSB is 0), number of set bits is same as i/2.
#    b. If i is odd (LSB is 1), number of set bits is 1 + number of set bits in i-1.
# 4. Return the result array.

class Solution:
   def countBits(self, n: int) -> List[int]:
       # Initialize result array with first element 0
       bitCounts = [0]
       
       # Calculate bit counts for numbers 1 to n
       for i in range(1, n + 1):
           if i % 2 == 0:  # Even number
               # For even number i, bits(i) = bits(i/2)
               # i >> 1 is equivalent to i/2
               bitCounts.append(bitCounts[i >> 1])
           else:  # Odd number
               # For odd number i, bits(i) = bits(i-1) + 1
               bitCounts.append(bitCounts[i - 1] + 1)
       
       return bitCounts
