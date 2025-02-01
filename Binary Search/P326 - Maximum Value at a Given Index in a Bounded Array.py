# Time Complexity:
# - O(log maxSum) due to binary search
# - Helper function calculation is O(1)
# - Overall complexity is O(log maxSum)

# Space Complexity:
# - O(1) as we only use a few variables
# - No extra space needed relative to input size

# INTUITION:
# Key insights:
# 1. Array should be mountain-shaped with peak at index
# 2. Numbers decrease by 1 in both directions from peak
# 3. Can't be negative, so flatten at 1 when needed
# Example: n=6, index=2, maxSum=10
# [1,2,3,2,1,1] peak=3 at index 2
# We binary search for optimal peak value
# For each peak value, calculate required sum
# using arithmetic sequence formula

# ALGO:
# 1. Binary search for peak value - 1
# 2. For each potential peak value:
#    Calculate sum needed using two parts:
#    a) Left side from start to index
#    b) Right side from index to end
# 3. For each part:
#    - Find where sequence flattens at 1
#    - Use arithmetic sequence sum formula
# 4. Compare total with maxSum-n
#    (subtract n because minimum array sum is n)

def maxValue(self, n: int, index: int, maxSum: int) -> int:
   def calculateSum(peakValue: int) -> int:
       # Calculate first number on left and right sides
       leftStart = max(peakValue - index, 0)
       rightStart = max(peakValue - (n - 1 - index), 0)
       
       # Calculate sums of arithmetic sequences on both sides
       # Formula: (first + last) * count / 2
       leftSum = (peakValue + leftStart) * (peakValue - leftStart + 1) / 2
       rightSum = (peakValue + rightStart) * (peakValue - rightStart + 1) / 2
       
       # Subtract peak value once as it's counted twice
       return leftSum + rightSum - peakValue
   
   # Subtract n from maxSum (account for minimum 1s)
   remainingSum = maxSum - n
   
   # Binary search for peak value - 1
   left, right = 0, remainingSum
   
   while left < right:
       mid = (left + right + 1) // 2
       if calculateSum(mid) <= remainingSum:
           left = mid
       else:
           right = mid - 1
   
   # Return peak value (add 1 back)
   return left + 1
