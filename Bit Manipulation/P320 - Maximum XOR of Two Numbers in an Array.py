# Time Complexity:
# - O(N * L), where N is length of nums array and L is max length of numbers in binary
# - For each bit position, need to check all number prefixes
# - Set operations are O(1) average case

# Space Complexity:
# - O(N) to store prefixes set for each bit position
# - Set can contain up to N prefixes

# INTUITION:
# Build maximum XOR bit by bit from left to right.
# For each bit position, try to set it to 1.
# Check if we can find two prefixes that XOR to give our candidate.
# If found, keep the 1 bit, otherwise use 0.

# ALGO:
# 1. Get maximum bit length needed (from largest number)
# 2. Build result from left to right:
#    - Left shift current result
#    - Try setting current bit to 1
#    - Get set of all number prefixes at current position
#    - Check if any two prefixes XOR to candidate
#    - If found, keep the 1 bit
# 3. Return final result

class Solution:
   def findMaximumXOR(self, nums: List[int]) -> int:
       # Get length of largest number in binary
       maxBitLength = len(bin(max(nums))) - 2  # Subtract "0b" prefix
       maxXOR = 0
       
       # Build result bit by bit from left to right
       for i in range(maxBitLength - 1, -1, -1):
           # Try to add 1 at current position
           maxXOR <<= 1
           currentCandidate = maxXOR | 1
           
           # Get all prefixes at current bit position
           prefixes = {num >> i for num in nums}
           
           # Check if we can achieve candidate
           if any((prefix ^ currentCandidate) in prefixes for prefix in prefixes):
               maxXOR = currentCandidate
               
       return maxXOR
