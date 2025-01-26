# Time Complexity: O(N)
# Space Complexity: O(1)

# INTUITION:
# Count partitions where sum of left and right parts are almost equal
# Check if difference between partitions is divisible by 2
# Stop before last element to ensure two-part partition

# ALGO:
# 1. Track running sum (current) and total array sum
# 2. Iterate through array (excluding last element)
# 3. For each iteration:
#    - Add current number to running sum
#    - Calculate remaining sum
#    - Check if absolute difference is even
#    - Increment result if condition met

class Solution:
   def countPartitions(self, nums: List[int]) -> int:
       result = 0
       currentSum = 0
       totalSum = sum(nums)

       for num in nums[:-1]:
           currentSum += num
           remainingSum = totalSum - currentSum
           if abs(remainingSum - currentSum) % 2 == 0:
               result += 1

       return result
