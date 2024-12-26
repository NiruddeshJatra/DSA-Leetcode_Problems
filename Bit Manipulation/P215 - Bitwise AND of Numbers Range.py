# Time Complexity:
# - O(log(max(left, right))), where `log` refers to the number of bits in the binary representation.
#   - The while loop executes at most as many times as the number of bits in the numbers.

# Space Complexity:
# - O(1), as we are using a constant amount of space.

# INTUITION:
# When performing a bitwise AND operation over a range `[left, right]`, bits that differ between `left` and `right` 
# will eventually turn to `0` in the AND result. The goal is to find the common prefix of `left` and `right` in binary form.

# ALGO:
# 1. Shift both `left` and `right` rightwards until they become equal. Each shift removes the least significant bit.
#    - This effectively eliminates any differing bits in the range `[left, right]`.
# 2. Keep a count of how many shifts were performed.
# 3. Once `left` and `right` are equal, shift the result back leftwards by the same count to restore the common prefix.
# 4. Return the result.

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0  # Track the number of shifts
        while left != right:  # Continue until left and right have the same binary prefix
            left >>= 1  # Right shift `left`
            right >>= 1  # Right shift `right`
            count += 1  # Increment the shift count

        # Shift the common prefix back to its original position
        return left << count
