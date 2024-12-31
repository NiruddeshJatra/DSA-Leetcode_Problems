# Time Complexity:
# - O(N) where N is length of binary string
#   - count() operation: O(N)
#   - find() operation: O(N)
#   - String concatenation: O(N)

# Space Complexity:
# - O(N) for creating new result string
#   - No additional data structures besides output string
#   - Space proportional to input length

# INTUITION:
# We can make binary string maximum by:
# - Understanding "00" -> "10" and "10" -> "01" operations
# - Observing that we can move zeros to the right
# - All zeros except one can be converted to ones
# - Optimal result will have single zero as far right as possible
# - Leading ones must stay in place as they can't be improved
# Final form: leading 1s + remaining 1s + single 0 + trailing 1s

# ALGO:
# 1. Count total zeros in string
# 2. Find position of first zero (leading ones)
# 3. If zeros ≤ 1, string already optimal
# 4. Calculate remaining ones after zeros
# 5. Construct result string:
#    - Leading + converted ones (leadingOnes + zeros - 1)
#    - Single zero
#    - Remaining original ones

class Solution:
   def maximumBinaryString(self, binary: str) -> str:
       # Count zeros and find first zero position
       zeros = binary.count('0')
       leadingOnes = binary.find('0')
       
       # Handle cases with 0 or 1 zero
       if zeros <= 1:
           return binary
           
       # Calculate remaining ones after zeros
       restOnes = len(binary) - leadingOnes - zeros
       
       # Construct maximum binary string
       return '1' * (leadingOnes + zeros - 1) + '0' + '1' * restOnes
