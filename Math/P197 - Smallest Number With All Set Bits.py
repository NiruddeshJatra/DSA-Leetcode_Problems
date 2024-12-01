# Time Complexity: O(log(n)), where log(n) is the number of bits required to represent n in binary.
# - Converting `n` to binary takes O(log(n)).
# - Computing the power of 2 also takes O(log(n)).

# Space Complexity: O(log(n)).
# - The binary representation of `n` requires O(log(n)) space.

# INTUITION:
# - The problem asks to find the smallest number in binary format that has all bits set to `1` 
#   and has a length equal to the binary representation of `n`.
# - For a number `n` in binary (e.g., `101`), the smallest number with the same number of bits all set to `1`
#   would be `111` (in binary) or `2^k - 1` (in decimal), where `k` is the number of bits.

# ALGORITHM:
# 1. Convert `n` to its binary representation and compute its length.
# 2. Calculate `2^k - 1`, where `k` is the number of bits in `n`'s binary representation.
# 3. Return the result.

class Solution:
    def smallestNumber(self, n: int) -> int:
        # Convert n to binary and find its length
        binary = bin(n)[2:]
        
        # Calculate the smallest number with all bits set to 1 for the given length
        return 2**len(binary) - 1

# Example Usage:
# Input: n = 5
# Binary representation: 5 = "101"
# Smallest number with 3 bits all set: "111" = 7
# Output: 7

# Input: n = 1
# Binary representation: 1 = "1"
# Smallest number with 1 bit all set: "1" = 1
# Output: 1

# Input: n = 15
# Binary representation: 15 = "1111"
# Smallest number with 4 bits all set: "1111" = 15
# Output: 15
