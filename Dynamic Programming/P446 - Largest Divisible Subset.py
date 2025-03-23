from sys import *
from collections import *
from math import *
from typing import List

class Solution:
   def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
       # Time Complexity:
       # - O(n²) where n is the length of the input array
       # - We use nested loops, with the outer loop running n times and inner loop running up to i times
       # - Sorting the array initially takes O(n log n) time
       
       # Space Complexity:
       # - O(n) for the dp array and prev array that track subset length and indices
       
       # INTUITION:
       # This problem is similar to Longest Increasing Subsequence (LIS), but with a divisibility condition
       # instead of an increasing condition. For a subset to be divisible, each pair of elements must be
       # divisible by each other. If we sort the array, we only need to check if nums[i] % nums[j] == 0,
       # since nums[i] will always be greater than or equal to nums[j].
       #
       # The key insight is that if a and b are divisible (a % b == 0) and b and c are divisible (b % c == 0),
       # then a and c are also divisible (a % c == 0). This transitive property allows us to build our subset
       # incrementally.
       #
       # For example, with array [1, 2, 4, 8]:
       # - 1 is divisible by itself
       # - 2 is divisible by 1, so the subset can be [1, 2]
       # - 4 is divisible by both 1 and 2, extending the subset to [1, 2, 4]
       # - 8 is divisible by all previous numbers, giving us [1, 2, 4, 8]
       
       # ALGO:
       # 1. Sort the array in ascending order
       # 2. Initialize a dp array where dp[i] represents the size of the largest divisible subset ending at index i
       # 3. Initialize a prev array to track the previous index in the subset
       # 4. For each position i, check all previous positions j:
       #    a. If nums[i] is divisible by nums[j] (nums[i] % nums[j] == 0) and including nums[i] leads to a larger subset,
       #       update dp[i] and prev[i]
       # 5. Find the index with the maximum dp value
       # 6. Reconstruct the subset using the prev array
       # 7. Return the largest divisible subset
       
       # Sort the array to ensure we only need to check one divisibility condition
       nums.sort()
       n = len(nums)
       
       # dp[i] represents the size of the largest divisible subset ending at index i
       dp = [1] * n
       
       # prev[i] stores the previous index in the subset
       prev = [-1] * n
       
       # Fill the dp and prev arrays
       for i in range(n):
           for j in range(i):
               # If nums[i] is divisible by nums[j] and including it leads to a larger subset
               if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                   dp[i] = dp[j] + 1  # Update the size of the subset
                   prev[i] = j  # Update the previous index
       
       # Find the index with the maximum dp value
       maxIndex = 0
       for i in range(n):
           if dp[i] > dp[maxIndex]:
               maxIndex = i
       
       # Reconstruct the subset using the prev array
       result = []
       while maxIndex != -1:
           result.append(nums[maxIndex])
           maxIndex = prev[maxIndex]
       
       # The result is constructed in reverse order, so we need to reverse it
       return result
