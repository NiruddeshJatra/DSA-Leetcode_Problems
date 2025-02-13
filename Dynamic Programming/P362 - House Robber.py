# Time Complexity:
# - O(N) where N is length of nums array
# - Single pass through array
# - Constant time operations at each step

# Space Complexity:
# - O(1) only using two variables
# - Space independent of input size

# INTUITION:
# Think of a burglar planning robberies on a street:
# - Can't rob adjacent houses (alarm systems connected)
# - At each house, must decide:
#   1. Rob current house + money from 2 houses back
#   2. Skip current house, keep money from previous house
#
# Example:
# [2, 7, 9, 3, 1]
# House 0: 2
# House 1: max(7, 2) = 7 
# House 2: max(9+2, 7) = 11
# House 3: max(3+7, 11) = 11
# House 4: max(1+11, 11) = 12

# ALGORITHM:
# Use dynamic programming with space optimization:
# - prev2: max money if we ended 2 houses back
# - prev1: max money if we ended at previous house
# - At each house:
#   1. Try including current (prev2 + num)
#   2. Try excluding current (prev1)
#   3. Take maximum and update state
#   4. Slide window forward

class Solution:
   def rob(self, nums: List[int]) -> int:
       # Handle edge cases
       if not nums:
           return 0
       if len(nums) == 1:
           return nums[0]
           
       # Initialize previous maximums
       twoHousesBack = 0  # Max money if we ended 2 houses back
       oneHouseBack = 0   # Max money if we ended at previous house
       
       # Process each house
       for currentMoney in nums:
           # Calculate current maximum
           # Either rob current house + money from 2 houses back
           # Or skip current house and keep money from previous house
           currentMax = max(twoHousesBack + currentMoney, oneHouseBack)
           
           # Slide window forward
           twoHousesBack = oneHouseBack
           oneHouseBack = currentMax
       
       return oneHouseBack  # Final maximum possible money
