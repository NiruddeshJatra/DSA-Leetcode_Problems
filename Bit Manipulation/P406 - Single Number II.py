# Time Complexity:
# - O(n), where n is the length of the input array.
# - We iterate through the array exactly once.

# Space Complexity:
# - O(1), as we only use two variables regardless of input size.

# INTUITION:
# In this problem, every number appears three times except for one number that appears only once.
# We need to find that unique number efficiently without using extra space.
#
# The key insight is to track how many times each bit has appeared modulo 3. If a bit appears
# 3 times, it should effectively disappear (0 mod 3). Only bits from the single number that 
# appears once will remain.
#
# We use two variables: 'ones' and 'twos' to track bits that have appeared once and twice respectively.
# - When a bit appears for the first time, it gets set in 'ones'
# - When a bit appears for the second time, it gets unset in 'ones' and set in 'twos'
# - When a bit appears for the third time, it gets unset in 'twos' (and remains unset in 'ones')
#
# After processing all numbers, 'ones' will contain the bits of the number that appears only once.

# ALGO:
# 1. Initialize two variables 'ones' and 'twos' to 0.
# 2. For each number in the array:
#    a. Update 'ones' to track bits that have appeared once (mod 3).
#    b. Update 'twos' to track bits that have appeared twice (mod 3).
#    c. Use bitwise operations to ensure each bit in 'ones' and 'twos' follows the rules:
#       - XOR (^) toggles bits based on the current number
#       - AND with complement (~) ensures bits don't appear in both 'ones' and 'twos'
# 3. Return 'ones', which contains the single number.

class Solution:
   def singleNumber(self, nums: List[int]) -> int:
       # Initialize counters for bits that have appeared once and twice
       bitsAppearingOnce = 0
       bitsAppearingTwice = 0
       
       # Process each number in the array
       for num in nums:
           # Update bits that have appeared once:
           # XOR with current number to toggle bits, then remove any bits that have appeared twice
           bitsAppearingOnce = (bitsAppearingOnce ^ num) & ~bitsAppearingTwice
           
           # Update bits that have appeared twice:
           # XOR with current number to toggle bits, then remove any bits that are now in 'once' state
           bitsAppearingTwice = (bitsAppearingTwice ^ num) & ~bitsAppearingOnce
       
       # After processing all numbers, bitsAppearingOnce contains the number that appears only once
       return bitsAppearingOnce
