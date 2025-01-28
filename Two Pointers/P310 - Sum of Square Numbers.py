# Time Complexity:
# - O(sqrt(c)), where c is the input number
# - We search through pairs of numbers up to sqrt(c)

# Space Complexity:
# - O(1), only uses constant extra space regardless of input size

# INTUITION:
# Use two pointers from 0 to sqrt(c) to find a pair of squares that sum to c.
# Start with smallest and largest possible values, adjust based on sum comparison.

# ALGO:
# 1. Initialize pointers at 0 and sqrt(c)
# 2. Calculate sum of squares at current pointers
# 3. If sum < target: increment left pointer for larger sum
# 4. If sum > target: decrement right pointer for smaller sum
# 5. If sum = target: found valid pair
# 6. Return false if no pair found

class Solution:
   def judgeSquareSum(self, c: int) -> bool:
       leftNum = 0
       rightNum = int(math.sqrt(c))
       
       while leftNum <= rightNum:
           currentSum = leftNum * leftNum + rightNum * rightNum
           
           if currentSum < c:
               leftNum += 1
           elif currentSum > c:
               rightNum -= 1
           else:
               return True
               
       return False
