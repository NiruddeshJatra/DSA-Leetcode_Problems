# Time Complexity: O(n), where n is the length of the input list `digits`.
# - We iterate over the digits from the last to the first to handle the addition.

# Space Complexity: O(1).
# - The operation is performed in place except for the final case where a new digit (1) is added, requiring O(n) space in the worst case.

# INTUITION:
# - When adding 1 to a number represented as an array of digits, you need to handle potential carry-over:
#   - If a digit becomes 10, it resets to 0, and the carry propagates to the next higher place value.
#   - If there is no carry left, the addition is complete, and we can terminate early.
# - If the carry remains after processing all digits (e.g., 999 + 1 = 1000), we prepend a `1` to the array.

# ALGORITHM:
# 1. Start with a carry of 1 since we're adding 1.
# 2. Traverse the `digits` array in reverse order (from the least significant digit to the most significant).
# 3. Add the carry to the current digit. If the sum equals 10, set the current digit to 0 and keep the carry as 1.
# 4. If the sum is less than 10, update the digit and reset the carry to 0, as no further propagation is needed.
# 5. If there is still a carry after the loop, prepend a 1 to the array.
# 6. Return the modified array.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Initial carry from adding 1

        # Traverse the digits from the least significant to the most significant
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += carry  # Add carry to the current digit
                if digits[i] == 10:  # Handle carry propagation
                    digits[i] = 0
                else:
                    carry = 0  # Reset carry if no further propagation is needed
            else:
                break  # If no carry is left, exit early

        # If there's still a carry, it means we need to add a new most significant digit
        if carry:
            return [1] + digits

        return digits

# Example Usage:
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
# Explanation: 123 + 1 = 124

# Input: digits = [9, 9, 9]
# Output: [1, 0, 0, 0]
# Explanation: 999 + 1 = 1000
