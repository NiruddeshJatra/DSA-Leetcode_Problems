# Time Complexity: O(n), where n is the length of the input list 'nums'.
# Space Complexity: O(n), for storing prefix sums in the dictionary.

# INTUITION:
# The code aims to find the maximum sum of a subarray within the input list 'nums' 
# such that the length of the subarray is constrained to be within 'k'. It uses a 
# prefix sum dictionary ('prefixSum') to efficiently calculate cumulative sums and 
# track the minimum prefix sum encountered so far. The 'maxSum' variable keeps track 
# of the maximum subarray sum found.

# ALGO:
# 1. Initialize variables: 'prefixSum' as a dictionary to store cumulative sums up 
#    to each index, 'maxSum' to store the maximum subarray sum, and 'currSum' to 
#    track the current cumulative sum.
# 2. Iterate through each element 'i' in the input list 'nums':
#    2.1. If 'i' is already present in 'prefixSum', update its value with the minimum 
#         of the current cumulative sum 'currSum' and the existing value.
#    2.2. If 'i' is not present in 'prefixSum', add it to the dictionary with the 
#         value of 'currSum'.
#    2.3. Update 'currSum' by adding the current element 'i'.
#    2.4. Iterate through the values of 'i + k' and 'i - k':
#         2.4.1. If the value is present in 'prefixSum', update 'maxSum' with the 
#                maximum of 'maxSum' and the difference between 'currSum' and the 
#                corresponding value in 'prefixSum'.
# 3. Return 'maxSum' as the result, which represents the maximum sum of a subarray 
#    within 'nums' with a length constraint of 'k'.

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}  # Dictionary to store cumulative sums.
        maxSum, currSum = -10 ** 18, 0  # Initialize variables.
        
        for i in nums:
            if i in prefixSum:
                prefixSum[i] = min(currSum, prefixSum[i])
            else:
                prefixSum[i] = currSum
            
            currSum += i
            
            for j in [i + k, i - k]:
                if j in prefixSum:
                    maxSum = max(maxSum, currSum - prefixSum[j])

        return maxSum  # Return the maximum subarray sum.
