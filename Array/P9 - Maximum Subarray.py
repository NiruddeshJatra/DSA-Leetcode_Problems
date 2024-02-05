# Time Complexity: O(n), where n is the length of the input list 'nums'.
# Space Complexity: O(1)

# INTUITION:
# The code aims to find the maximum sum of a contiguous subarray within the input list 
# 'nums'. It iterates through the elements of 'nums' while maintaining two variables: 
# 'currSum' to keep track of the current sum of the subarray, and 'maxSum' to store the 
# maximum sum found so far. If the current sum becomes negative, it resets 'currSum' to 
# 0. It updates 'maxSum' with the maximum of 'maxSum' and 'currSum' in each iteration 
# and returns 'maxSum' as the result.

# ALGO:
# 1. Initialize variables: 'currSum' to track the current sum of subarrays, and 'maxSum' 
#    to store the maximum sum found so far. Set 'maxSum' to a very small number to handle 
#    negative input values.
# 2. Iterate through each element 'i' in the input list 'nums':
#    2.1. If 'currSum' becomes negative, reset it to 0, as we are looking for the maximum 
#         sum of contiguous subarrays.
#    2.2. Update 'currSum' by adding the current element 'i'.
#    2.3. Update 'maxSum' with the maximum of 'maxSum' and 'currSum' in each iteration.
# 3. Return 'maxSum' as the result, which represents the maximum sum of a contiguous 
#    subarray within 'nums'.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0  # Initialize current sum of subarrays.
        maxSum = -10 ** 18  # Initialize maximum sum found so far.
        for i in nums:
            if currSum < 0:  # Reset current sum if it becomes negative.
                currSum = 0
            currSum += i  # Update current sum by adding the current element.
            maxSum = max(maxSum, currSum)  # Update maximum sum.
        return maxSum  # Return the maximum sum found.
