# Time Complexity:
# - O(log n), where n is the input number
# - Each recursive call divides n by 5, leading to logarithmic number of calls
# - The actual number of operations is log(n) to the base 5

# Space Complexity:
# - O(log n) for the recursive call stack
# - Each recursive call takes constant space, with log(n) total calls

# INTUITION:
# The problem asks for the number of trailing zeros in n!
# Key insight:
# - Trailing zeros are formed by factors of 10 (2×5)
# - Since there are always more factors of 2 than factors of 5 in n!,
#   we only need to count the factors of 5
# Example:
# For n = 25:
# - Numbers contributing one factor of 5: 5, 10, 15, 20, (5 numbers)
# - Numbers contributing two factors of 5: 25 (1 number)
# - Total factors of 5: 5 + 1 = 6
# - Therefore, 25! has 6 trailing zeros

# ALGO:
# 1. Count how many multiples of 5 are in the range [1,n]
# 2. Count how many multiples of 25 are in the range [1,n]
# 3. Count how many multiples of 125 are in the range [1,n]
# 4. Continue this process until n/5^k becomes 0
# 5. The recursive approach elegantly handles this by:
#    - First counting n/5 (multiples of 5)
#    - Then recursively counting (n/5)/5 (multiples of 25)
#    - And so on until the base case is reached

class Solution:
   def trailingZeroes(self, n: int) -> int:
       # Base case: no trailing zeros for 0!
       if n == 0:
           return 0
           
       # Count factors of 5 in n!
       # First count direct multiples of 5
       # Then recursively count multiples of higher powers of 5
       return n // 5 + self.trailingZeroes(n // 5)
