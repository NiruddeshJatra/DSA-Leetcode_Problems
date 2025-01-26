# Time Complexity: O(N * U), where N is array length, U is unique values
# Space Complexity: O(1) additional space

# INTUITION:
# Find maximum frequency achievable by incrementing values
# Track increments for each unique target value
# Count occurrences of target value k separately

# ALGO:
# 1. Iterate through unique values
# 2. Track current and max increments
# 3. Count valid increments per unique value
# 4. Add occurrences of k to final result

class Solution:
   def maxFrequency(self, nums: List[int], k: int) -> int:
       maxFreq = 0
       uniqueValues = set(nums)
       
       for target in uniqueValues:
           if target == k:
               continue
           
           currentIncrement = maxIncrement = 0
           for num in nums:
               if num == k:
                   currentIncrement -= 1
               elif num == target:
                   currentIncrement += 1
               
               currentIncrement = max(currentIncrement, 0)
               maxIncrement = max(maxIncrement, currentIncrement)
           
           maxFreq = max(maxFreq, maxIncrement)
       
       return maxFreq + nums.count(k)
