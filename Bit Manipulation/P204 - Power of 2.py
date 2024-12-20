# Time Complexity: O(1).  
# - The bitwise operation `n & (n - 1)` is performed in constant time, and the additional comparisons (`n > 0` and `not n & (n - 1)`) also take constant time.  
# - Therefore, the overall time complexity is O(1).

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space for variables and operations.  

# INTUITION:  
# A number `n` is a power of two if it has exactly one bit set to 1 in its binary representation.  
# For example:  
# - 1 (2^0) -> 0001  
# - 2 (2^1) -> 0010  
# - 4 (2^2) -> 0100  
# - 8 (2^3) -> 1000  
# Notice that for all powers of two, `n & (n - 1)` results in 0.  
# This is because subtracting 1 from `n` flips all the bits after the rightmost set bit, and the bitwise AND of `n` and `n - 1` clears that set bit.  

# ALGO:  
# 1. Check if `n` is greater than 0.  
#    - If `n` is non-positive, return `False` immediately since no power of two can be negative or zero.  
# 2. Use the condition `n & (n - 1) == 0` to check if `n` is a power of two.  
#    - If the condition is true, return `True`.  
#    - Otherwise, return `False`.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0 and if n & (n - 1) is 0
        if n > 0 and not n & (n - 1):
            return True
        return False
