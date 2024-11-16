# Time Complexity: O(1)  
# The solution directly calculates the number of operations based on the length of the array `n`,  
# requiring only a few arithmetic operations.

# Space Complexity: O(1)  
# No additional space is used beyond a few variables for calculations.

# INTUITION:  
# The array is defined as `arr[i] = 2 * i + 1` for all `0 <= i < n`.  
# This generates an array of odd numbers, e.g., `[1, 3, 5, 7, 9]` for `n=5`.  
# To make all elements equal, the array needs to be transformed so that all elements  
# become equal to the mean of the array.  

# For this specific problem, the mean is always the middle value of the array if `n` is odd,  
# or the average of the two middle values if `n` is even.  
# The key insight is to observe that the number of operations needed to make all elements equal  
# is determined by the sum of differences between elements in the first half and the middle value.  
# This sum can be calculated mathematically as a pattern:  
# - If `n` is even: `(n//2)**2`  
# - If `n` is odd: `(n//2) * (n//2 + 1)`  

# ALGO:  
# 1. Check whether `n` is even or odd.  
# 2. If `n` is even, calculate the result as `(n//2)**2`.  
# 3. If `n` is odd, calculate the result as `(n//2) * (n//2 + 1)`.  
# 4. Return the result.

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n // 2) ** 2
        return (n // 2) * (n // 2 + 1)
