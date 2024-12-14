# Time Complexity: O(max(len(a), len(b))), where len(a) and len(b) are the lengths of the input binary strings.  
# - The zfill operation takes O(max(len(a), len(b))) time to pad the shorter string.  
# - The iteration through the binary strings also takes O(max(len(a), len(b))).  
# Hence, the overall complexity is O(max(len(a), len(b))).

# Space Complexity: O(max(len(a), len(b))), where len(a) and len(b) are the lengths of the input binary strings.  
# - The result string `res` grows to the size of the longer string, resulting in O(max(len(a), len(b))) space usage.  
# - The additional space for variables like `carry` and the temporary sum is O(1).  

# INTUITION:  
# To add two binary numbers, we can simulate the addition process digit by digit (from right to left) while keeping track of a carry value.  
# By equalizing the lengths of the two strings using zero padding (`zfill`), we can process the corresponding bits directly.  
# At each step, the current digit is determined by the sum of the corresponding bits and the carry, modulo 2.  
# The carry for the next iteration is calculated by dividing the current sum by 2.  
# After processing all digits, if there is a leftover carry, it is appended to the result.  
# The result is built in reverse order and reversed at the end to form the final binary sum.

# ALGO:  
# 1. Equalize the lengths of `a` and `b` by zero-padding the shorter string.  
# 2. Initialize an empty string `res` to store the binary result and a `carry` variable set to 0.  
# 3. Iterate through both strings from the rightmost digit to the leftmost:  
#    - Compute the sum of the digits and the carry.  
#    - Append the current digit (sum modulo 2) to the result string.  
#    - Update the carry (sum divided by 2).  
# 4. After the loop, check if there is any leftover carry and append it to `res`.  
# 5. Reverse the result string and return it.

from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0

        # Equalize the lengths of the strings
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))

        # Traverse the strings from right to left
        i = len(a) - 1
        while i >= 0:
            curSum = int(a[i]) + int(b[i]) + carry  # Sum of corresponding digits and carry
            carry = curSum // 2  # Update carry
            res += str(curSum % 2)  # Append the current digit to the result
            i -= 1

        # Append leftover carry if present
        if carry:
            res += '1'

        # Reverse the result to get the correct binary sum
        return res[::-1]
