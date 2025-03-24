# Time Complexity:
# - O(N*K), where N is the length of the array and K is the maximum partition size
# - We iterate through the array, and for each element, we consider up to K next elements
# - Each iteration involves finding the maximum element in a subarray

# Space Complexity:
# - O(N) for the dynamic programming array
# - Additional O(N) space used by the recursion stack (memoization approach)

# INTUITION:
# The problem requires maximizing the sum by partitioning the array into subarrays
# Key strategy:
# - Divide the array into subarrays of maximum length K
# - For each subarray, replace all elements with the maximum element
# - Goal is to maximize the total sum after this transformation
# Example:
# arr = [1,15,7,9,2,5,10], k = 3
# Optimal partitioning:
# [1,15,7] → max is 15, sum becomes 15*3 = 45
# [9,2,5] → max is 9, sum becomes 9*3 = 27
# [10]    → max is 10, sum becomes 10*1 = 10
# Total maximum sum: 45 + 27 + 10 = 82

# ALGO:
# 1. Use dynamic programming to solve the problem
# 2. Work backwards through the array
# 3. For each index, try all possible partitions of length up to K
# 4. Calculate the maximum possible sum by:
#    - Finding the maximum element in the current partition
#    - Multiplying max element by partition length
#    - Adding the maximum sum from the rest of the array
# 5. Memoize results to avoid recomputing subproblems

class Solution:
   def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
       n = len(arr)
       # Initialize DP array to store maximum sum for each starting index
       dp = [0] * (n + 1)

       # Iterate backwards through the array
       for currentIndex in range(n - 1, -1, -1):
           # Track maximum sum for current index
           currentMaxSum = float('-inf')
           
           # Try all possible partition lengths up to k
           for partitionEnd in range(currentIndex, min(currentIndex + k, n)):
               # Find maximum element in current partition
               currentPartitionMax = max(arr[currentIndex:partitionEnd+1])
               
               # Calculate sum for current partition
               # Multiply max element by partition length 
               # Add maximum sum from remaining array
               partitionSum = (
                   currentPartitionMax * (partitionEnd - currentIndex + 1) + 
                   dp[partitionEnd + 1]
               )
               
               # Update maximum sum for current index
               currentMaxSum = max(currentMaxSum, partitionSum)
           
           # Store maximum sum for current starting index
           dp[currentIndex] = currentMaxSum
       
       # Return maximum sum for entire array
       return dp[0]
